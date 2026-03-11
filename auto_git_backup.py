# pip install watchdog
# python auto_git_backup.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class AutoGitHandler(FileSystemEventHandler):
    last_commit_time = 0  # cooldown timer

    def on_modified(self, event):
        # Ignore directories and unwanted folders
        if event.is_directory:
            return
        if any(x in event.src_path for x in [".git", "venv"]):
            return

        # Cooldown: only commit once every 3 seconds to avoid double commits
        now = time.time()
        if now - AutoGitHandler.last_commit_time < 3:
            return
        AutoGitHandler.last_commit_time = now

        print(f"Change detected: {event.src_path}")

        # Commit all tracked changes automatically (-a) with a short message
        result = subprocess.run(
            ["git", "commit", "-a", "-m", f"Auto update: {event.src_path}"],
            capture_output=True,
            text=True
        )

        if "nothing to commit" in result.stdout.lower():
            print("No changes to commit.")
        else:
            # Push after commit
            subprocess.run(["git", "push"])
            print(f"✅ Backup pushed with message: Auto update: {event.src_path}")

if __name__ == "__main__":
    path = os.getcwd()  # Watch the current project
    event_handler = AutoGitHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Watching for changes (press Ctrl+C to stop)...")
    try:
        while True:
            time.sleep(1)  # keeps observer alive
    except KeyboardInterrupt:
        observer.stop()
    observer.join()