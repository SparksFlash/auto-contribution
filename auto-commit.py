import os
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = "/home/sourav/auto-contribution/"  # Replace with your repository path
FILE_TO_UPDATE = "daily_log.txt"  # File to modify for commit
BRANCH = "main"  # Replace with your branch name if different

def run_command(command, cwd=None):
    """Run a shell command and handle errors."""
    try:
        result = subprocess.run(command, cwd=cwd, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command {' '.join(command)}: {e.stderr}")
        exit(1)

def auto_commit():
    """Perform automated commit and push."""
    # Change to repository directory
    os.chdir(REPO_PATH)

    # Create or update the file with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_TO_UPDATE, "a") as f:
        f.write(f"Automated update at {timestamp}\n")

    # Git commands
    run_command(["git", "add", FILE_TO_UPDATE])
    run_command(["git", "commit", "-m", f"Daily automated commit: {timestamp}"])
    run_command(["git", "push", "origin", BRANCH])

    print(f"Successfully committed and pushed at {timestamp}")

if __name__ == "__main__":
    auto_commit()
