# pip install watchdog
# python auto_git_backup.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class AutoGitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # ignore folders and unwanted files
        if event.is_directory:
            return
        if any(x in event.src_path for x in [".git", "venv"]):
            return

        print(f"Change detected: {event.src_path}")

        # Add, commit, push
        subprocess.run(["git", "add", "."])
        subprocess.run([
            "git",
            "commit",
            "-m",
            f"auto backup {time.strftime('%Y-%m-%d %H:%M:%S')}"
        ])
        subprocess.run(["git", "push"])
        print("✅ Backup pushed")

if __name__ == "__main__":
    path = os.getcwd()  # watch current project
    event_handler = AutoGitHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Watching for changes (press Ctrl+C to stop)...")
    try:
        while True:
            time.sleep(1)  # keeps observer alive without locking terminal
    except KeyboardInterrupt:
        observer.stop()
    observer.join()