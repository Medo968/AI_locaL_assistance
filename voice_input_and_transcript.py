import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from faster_whisper import WhisperModel
import main

recording = False
stream = None
audio_data = []
sample_rate = 16000

model = WhisperModel(
    main.whisper_model,
    device=main.compute_device,
    compute_type=main.compute_type
)

# callback ONLY records audio
def callback(indata, frames, time, status):
    if recording:
        audio_data.append(indata.copy())


def start_recording():
    global stream, recording, audio_data

    audio_data = []
    recording = True

    stream = sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        callback=callback
    )
    stream.start()

    return "Recording started..."


def stop_recording(filename="output.wav"):
    global stream, recording, audio_data

    recording = False

    if stream:
        stream.stop()
        stream.close()
        stream = None

    if len(audio_data) == 0:
        return ""

    # merge chunks
    audio = np.concatenate(audio_data, axis=0)

    # save file AFTER recording is finished
    write(filename, sample_rate, audio)

    # 🧠 NOW transcription happens (NOT real-time)
    segments, info = model.transcribe(filename)

    text = " ".join(segment.text for segment in segments)

    return text.strip()