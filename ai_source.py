import requests
import main
def ai_s(type, content):
    if type == "ollama":
        return ask_ollama(content, main.model)
    elif type == "nvidia":
        return ask_nvidia(content)
    else:
        return "Unknown AI type"
def ask_ollama(prompt, model):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    return response.json()["response"]

API_KEY = "YOUR_NVIDIA_API_KEY"

url = "https://integrate.api.nvidia.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "meta/llama-3.1-8b-instruct",
    "messages": [
        {"role": "user", "content": "Hello, explain AI simply"}
    ],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

print(response.json()["choices"][0]["message"]["content"])
def ask_nvidia(prompt):
    print("not dupported till now")
#done