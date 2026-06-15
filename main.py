import resources
import os_battery as ob
import compute
import time 
import psutil as ps
import compute as cp
import voice_input_and_transcript as vit
import time
import sys
import control 
import apps
import random as rn
import ai_source 
global_settings = {
    "ai_type" : "ollama",
    "compute_device": cp.gpu_info().results[0],
}
model = "qwen3.5:cloud"
whisper_model = "tiny"
compute_type = "int8"
work = "work now"
oss = ob.get_os(ob.oss)
dtype = ob.device_type()
run = True
random = rn.random
nsupport = "not supported platform"
loadsign = ["|", "/", "-", "\\"]


def system_start(sup):
    while run:
        loading(sup)
        ob.user_device_name()
        cmd = input(">> ")
        if cmd[0] == "/":
            cmd_s = cmd.replace("/","")
            cmd_ss = cmd_s.lower()
            if cmd_ss[:len("search")] == "search":
                url = cmd_ss.replace("search","")
                control.open_the_app(apps.apps["edge"],"search",url)
            elif cmd_ss[:len("open")] == "open":
                app = cmd_ss.replace("open","")
                control.open_the_app(apps.apps[app],"open",url)
                if apps.apps[app] not in apps.apps:
                    print("that app({app}) isn't in the system")
            elif cmd_ss[:len("prompt")] == "prompt":
                prompt = cmd_ss.replace("prompt","")
                ai_source.ai_s(global_settings["ai_type"],prompt)
            elif cmd_ss[:len("edit")] == "edit":
                print(global_settings)
                which = input("which u want to edit")
                if which.lower() == "ai_type":
                    if global_settings["ai_type"] == "ollama":
                        current_ollama = work
                        current_nvidia = " "
                    else:
                        current_ollama = " "
                        current_nvidia = work
                    change = input(f"ollama(1){current_ollama}, nvidia(2){current_nvidia}")
                    if change in ["ollama","1"] and global_settings["ai_type"] == "nvidia":
                        global_settings["ai_type"] = "ollama"
                    elif change in ["nvidia","2"] and global_settings["ai_type"] == "ollama":
                        global_settings["ai_type"] = "nvidia"
        else:
            ai_source.ai_s(global_settings["ai_type"],prompt)
            
            
def breaker():
    return True

def loading(support):
    while True:
        for i in loadsign:
            sys.stdout.write("\r" + i)
            sys.stdout.flush()
            time.sleep(0.1)
            if support == True:
                break
            else:
                breaker()
                
def unsupported():
    print("unsupported")
    global run 
    run = False
    
match oss , dtype:
    case "windows" , "holdable":
        support = True
        system_start(support)
    case "windows" , "desktop":
        ...
    case "linux" , "holdable":
        ...
    case "linux" , "desktop":
        ...
    case "android" , "desktop":
        print("error how?")
    case "android" , "holdable":
        print(nsupport)
    case "macos" , "desktop":
        print(nsupport)
    case "macos" , "holdable":
        print(nsupport)
'''
pipline:
take order either as text or voice 
if text cmd or prompt
    / mean cmd
    normal text = prompt
    if cmd go to the system and to what u want 
    if prompt go ai with system prompt
if 
'''

            