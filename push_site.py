import subprocess

subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "markdown updated"], check=True)
subprocess.run(["git", "push"], check=True)

print("Pushed to remote.")
