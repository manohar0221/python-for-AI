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

        # Normalize file path for cross-platform compatibility
        filepath = event.src_path.replace("\\", "/")

        # Ignore .git folder and venv folder
        if filepath.startswith(".git/") or "/venv/" in filepath:
            return

        # Track changed files
        with self.lock:
            self.changed_files.add(filepath)

        # Reset/start 10-second timer for batch commit
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

        # Commit each file individually with an appropriate message
        for f in files:
            filename = os.path.basename(f)

            # Determine commit message based on file type
            if filename.endswith(".py"):
                msg = f"Code updated in {filename}"
            else:
                msg = f"File updated {filename}"

            # Stage and commit this file
            subprocess.run(["git", "add", f], capture_output=True, text=True)
            status = subprocess.run(
                ["git", "status", "--porcelain", f],
                capture_output=True,
                text=True
            ).stdout.strip()

            if not status:
                print(f"No changes to commit for {filename}.")
                continue

            subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
            subprocess.run(["git", "push"], capture_output=True, text=True)
            print(f"✅ Backup pushed with message: {msg}")


if __name__ == "__main__":
    path = os.getcwd()  # Watch the current project folder
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