#Add Memory
import json

def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f)

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}