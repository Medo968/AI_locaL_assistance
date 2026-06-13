import os
import platform
import psutil
# battery case
# battery percentage 
#os type 
#is holdable
oss = platform.platform()
battery = psutil.sensors_battery()
def get_os(oss):
    match oss[:3]:
        case "win":
            return "windows"
        case "lin":
            if os.environlinux("And"):
                return "android"
            else:
                return "linux"
        case "dar":
            return "macos"
def device_type():
    if psutil.sensors_battery <= -1:
        dtype = "holdable"
    else:
        dtype = "desktop"
    return dtype
def battery_percentage():
    if device_type() == "desktop":
        battery = None
    else:
        battery = psutil.sensors_battery()
    return battery
def battery_case():
    if device_type() == "desktop":
        battery_c = "cannot be charged"
    else:
        if battery is not None:
            if battery.power_plugged:
                battery_c = "charging"
            else:
                battery_c = "not charging"
    return battery_c






            