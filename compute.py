import wmi
import psutil
import vulkan as vk

c = wmi.WMI()
compute_way_list = ["cuda", "vulkan", "metal", "rocm", "cpu"]


def to_gb(x):
    if not x:
        return 0
    return round(x / (1024 ** 3), 2)

def check_vulkan():
    try:
        app_info = vk.VkApplicationInfo(
            pApplicationName="Test",
            applicationVersion=1,
            pEngineName="Test",
            engineVersion=1,
            apiVersion=vk.VK_API_VERSION_1_0
        )

        instance_info = vk.VkInstanceCreateInfo(
            pApplicationInfo=app_info
        )

        instance = vk.vkCreateInstance(instance_info, None)
        vk.vkDestroyInstance(instance, None)

        return True
    except:
        return False
def gpu_info():
    gpus = []

    for gpu in c.Win32_VideoController():
        name = gpu.Name.lower()

        if "nvidia" in name:
            company = "nvidia"
            backend = "cuda"
        elif "amd" in name or "radeon" in name:
            company = "amd"
            backend = "rocm"
        elif "intel" in name:
            company = "intel"
            backend = "oneapi"  # or cpu fallback
        else:
            company = "unknown"
            backend = "cpu"

        vram = getattr(gpu, "AdapterRAM", None)
        shared = getattr(gpu, "SharedSystemMemory", None)

        gpus.append({
            "name": gpu.Name,
            "company": company,
            "backend": backend,
            "vram": vram,
            "shared_memory": shared
        })

    return gpus