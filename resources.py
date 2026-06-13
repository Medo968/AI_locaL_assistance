import psutil
import gpu_system
import time


gpu_list = gpu_system.get_gpu_data()
device = {
    "cpu_usage": psutil.cpu_percent(interval=1),
    "ram_usage": psutil.virtual_memory().percent,
    "swap_usage": psutil.swap_memory().percent,
    "cpu_temp": gpu_system.cpu_temp(),
    "gpu_usage": gpu_system.gpu_usage(),
    "gpus": gpu_list
}
