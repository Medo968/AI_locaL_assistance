import psutil
import compute as cp
import time


gpu_list = cp.get_gpu_data()
device = {
    "cpu_usage": psutil.cpu_percent(interval=1),
    "ram_usage": psutil.virtual_memory().percent,
    "swap_usage": psutil.swap_memory().percent,
}