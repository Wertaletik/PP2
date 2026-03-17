import os
from pathlib import Path


os.makedirs("./practice6/1/2/3", exist_ok=True)

print("Current Directory Contents:", os.listdir("./practice5"))

py_files = [f for f in os.listdir("./practice5") if f.endswith(".py")]
print(f"Python files found: {py_files}")