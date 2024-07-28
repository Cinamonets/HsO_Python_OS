# utils/helpers.py
import json

registry = True
helpers = True

def greet(name):
    return f"Hello, {name}! Welcome to HsO."

def save_memory_status(status, file_path):
    with open(file_path, 'w') as f:
        json.dump(status, f, indent=4)

def read_memory_status(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
