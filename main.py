import resources
import os_battery as ob
import compute as cp
import time
import psutil
import voice_input_and_transcript as vit
import sys
import control
import apps
import random as rn
import ai_source
global_settings = {
    "ai_type": "ollama",
}
model = "qwen3.5:cloud"
compute_type = "int8"
whisper_model = "tiny"
run = True
loadsign = ["|", "/", "-", "\\"]
def system_start(sup):
    while run:
        loading(sup)
        ob.user_device_name()

        cmd = input(">> ")

        if cmd.startswith("/"):
            cmd_s = cmd.replace("/", "")
            cmd_ss = cmd_s.lower()
            if cmd_ss.startswith("search"):
                url = cmd_ss.replace("search", "").strip()
                control.search_edge(apps.apps["edge"], url)

            elif cmd_ss.startswith("open"):
                app = cmd_ss.replace("open", "").strip()

                if app in apps.apps:
                    control.open_app(apps.apps[app])
                else:
                    print(f"that app ({app}) isn't in the system")

            # PROMPT AI
            elif cmd_ss.startswith("prompt"):
                prompt = cmd_ss.replace("prompt", "").strip()

                result = ai_source.ai_s(
                    global_settings["ai_type"],
                    prompt,
                    model
                )

                print(result)

            # EDIT SETTINGS
            elif cmd_ss.startswith("edit"):
                print(global_settings)

                which = input("which u want to edit: ")

                if which.lower() == "ai_type":
                    change = input("ollama(1) / nvidia(2): ").strip()

                    if change in ["1", "ollama"]:
                        global_settings["ai_type"] = "ollama"

                    elif change in ["2", "nvidia"]:
                        global_settings["ai_type"] = "nvidia"

                    print("updated:", global_settings["ai_type"])

        else:
            # normal text → AI prompt
            prompt = cmd.strip()

            result = ai_source.ai_s(
                global_settings["ai_type"],
                prompt,
                model
            )

            print(result)


def loading(support):
    for i in loadsign:
        sys.stdout.write("\r" + i)
        sys.stdout.flush()
        time.sleep(0.1)

        if support:
            break


def unsupported():
    print("unsupported")
    global run
    run = False


match ob.get_os(ob.oss), ob.device_type():

    case "windows", "holdable":
        system_start(True)

    case "windows", "desktop":
        system_start(True)

    case "linux", "holdable":
        system_start(True)

    case "linux", "desktop":
        system_start(True)

    case "android", _:
        print("unsupported system")

    case "macos", _:
        print("unsupported system")