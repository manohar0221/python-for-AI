# pip install watchdog
# python auto_git_backup.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class AutoGitHandler(FileSystemEventHandler):
    last_commit_time = 0  # Cooldown timer

    def on_modified(self, event):
        # Ignore directories and unwanted folders
        if event.is_directory:
            return
        if any(x in event.src_path for x in [".git", "venv"]):
            return

        # Cooldown: only commit once every 3 seconds
        now = time.time()
        if now - AutoGitHandler.last_commit_time < 3:
            return
        AutoGitHandler.last_commit_time = now

        # Normalize file path
        filepath = event.src_path.replace("\\", "/")
        filename = os.path.basename(filepath)

        print(f"Change detected: {filepath}")

        # Stage changes
        subprocess.run(["git", "add", "."], capture_output=True, text=True)

        # Check for staged changes
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True
        ).stdout.strip()

        if not status:
            print("No changes to commit.")
            return

        # Determine commit message
        if "/data/" in filepath:
            msg = f"Data update in {filename}"
        elif filepath.endswith(".py"):
            msg = f"Code update in {filename}"
        else:
            msg = f"Update in {filename}"  # fallback for other files

        # Commit & push
        subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
        subprocess.run(["git", "push"], capture_output=True, text=True)
        print(f"✅ Backup pushed with message: {msg}")

if __name__ == "__main__":
    path = os.getcwd()  # Watch current project folder
    event_handler = AutoGitHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Watching for changes (press Ctrl+C to stop)...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()