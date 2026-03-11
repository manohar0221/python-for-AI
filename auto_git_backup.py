import subprocess
import time

while True:
    # check if there are changes
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )

    if result.stdout.strip():
        print("Changes detected → committing")

        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"auto backup {time.strftime('%Y-%m-%d %H:%M:%S')}"])
        subprocess.run(["git", "push"])

        print("Backup pushed")

    time.sleep(60)  # check every 60 seconds