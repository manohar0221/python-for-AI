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

        # Normalize path (important for Windows)
        filepath = event.src_path.replace("\\", "/")

        # Ignore .git internal files and virtual environment
        if "/.git/" in filepath or "/venv/" in filepath:
            return

        with self.lock:
            self.changed_files.add(filepath)

        # Restart 60 second timer
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

        print(f"Changes detected: {files}")

        for f in files:

            filename = os.path.basename(f)

            # Commit message rule
            if filename.endswith(".py"):
                msg = f"Code update in {filename}"
            else:
                msg = f"File updated {filename}"

            # Stage file
            subprocess.run(["git", "add", f], capture_output=True, text=True)

            # Check if staged changes exist
            status = subprocess.run(
                ["git", "diff", "--cached", "--name-only", f],
                capture_output=True,
                text=True
            ).stdout.strip()

            if not status:
                print(f"No changes to commit for {filename}")
                continue

            # Commit and push
            subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
            subprocess.run(["git", "push"], capture_output=True, text=True)

            print(f"✅ Backup pushed: {msg}")


if __name__ == "__main__":

    path = os.getcwd()

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
    