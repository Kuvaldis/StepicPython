import zipfile
import os
import os.path

def process(name):
    with zipfile.ZipFile(name + ".zip", "r") as zip:
        zip.extractall("./")
    with_py = [current_dir for current_dir, _, files in os.walk(name) if any([file for file in files if file.endswith(".py")])]
    print("\n".join(sorted(with_py)))

process("main")
