# pip install watchdog
# python auto_git_backup.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os
import threading

class AutoGitHandler(FileSystemEventHandler):
    def __init__(self):
        self.changed_files = set()
        self.lock = threading.Lock()
        self.timer = None

    def on_modified(self, event):
        if event.is_directory:
            return
        if any(x in event.src_path for x in [".git", "venv"]):
            return

        filepath = event.src_path.replace("\\", "/")
        with self.lock:
            self.changed_files.add(filepath)

        # Reset/start the timer
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(10, self.commit_and_push)
        self.timer.start()

    def commit_and_push(self):
        with self.lock:
            if not self.changed_files:
                return
            files = list(self.changed_files)
            self.changed_files.clear()

        print(f"Changes detected in: {', '.join(files)}")

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
        filenames = [os.path.basename(f) for f in files]
        msg = "Update in " + ", ".join(filenames)
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