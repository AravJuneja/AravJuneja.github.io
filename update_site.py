import re
import subprocess

with open("content.md") as f:
    content = f.read().strip()

with open("index.html") as f:
    html = f.read()

escaped = content.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")
updated = re.sub(r"(const md = `)[^`]*(`;)", f"\\1{escaped}\n\\2", html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(updated)

print("index.html updated.")

subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "markdown updated"], check=True)
subprocess.run(["git", "push"], check=True)

print("Pushed to remote.")
