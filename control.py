import subprocess
import os
import time
import apps

def open_vscode_with_command():
    try:
        subprocess.Popen(["code", "."])
        print("[OK] VS Code opened using 'code' command")
    except Exception as e:
        print("[FAIL] code command failed:", e)


def open_vscode_with_path():
    if os.path.exists(apps.apps["steam"]):
        subprocess.Popen([apps.apps["steam"]])
        print("[OK] VS Code opened using path:", apps.apps["steam"])
        return

print("[FAIL] VS Code exe not found")


if __name__ == "__main__":
    print("Opening VS Code...")

    open_vscode_with_command()
    time.sleep(2)
    open_vscode_with_path()