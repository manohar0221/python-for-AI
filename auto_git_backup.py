# pip install watchdog
# python auto_git_backup.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class AutoGitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Ignore directories and unwanted folders
        if event.is_directory:
            return
        if any(x in event.src_path for x in [".git", "venv"]):
            return

        print(f"Change detected: {event.src_path}")

        # Stage all changes first
        subprocess.run(["git", "add", "."])

        # Check staged changes
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True,
            text=True
        )
        files = result.stdout.strip().split("\n")

        if files != [""]:
            # Commit message based on changed files
            msg = f"Updated: {', '.join(files)}"

            # Commit & push
            subprocess.run(["git", "commit", "-m", msg])
            subprocess.run(["git", "push"])

            print(f"✅ Backup pushed with message: {msg}")
        else:
            print("No changes to commit.")

if __name__ == "__main__":
    path = os.getcwd()  # Watch the current project
    event_handler = AutoGitHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Watching for changes (press Ctrl+C to stop)...")
    try:
        while True:
            time.sleep(1)  # Keeps observer alive without blocking
    except KeyboardInterrupt:
        observer.stop()
    observer.join()