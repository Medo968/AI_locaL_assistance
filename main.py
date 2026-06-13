import resources
import os_battery as ob
import compute
import time 
import psutil as ps
import compute as cp
import voice_input_and_transcript as vit
model = "qwen3.5:cloud"
whisper_model = "tiny"
compute_device = cp.gpu_info().results[0]
compute_type = "int8"
oss = ob.get_os(ob.oss)
match oss:
    case "windows":
        dtype = ob.




