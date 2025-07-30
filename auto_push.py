import subprocess
import sys

def auto_push(commit_message="Auto update from script"):
    try:
        subprocess.check_call(["git", "add", "."])
        subprocess.check_call(["git", "commit", "-m", commit_message])
        subprocess.check_call(["git", "push"])
        print("Pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Auto git add, commit, and push.")
    parser.add_argument('-m', '--message', type=str, default="Auto update from script", help='Commit message')
    args = parser.parse_args()
    auto_push(args.message)
