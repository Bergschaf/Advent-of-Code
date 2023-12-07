import os
import shutil

day_number = 7

if os.path.exists(f"{day_number}"):
    print("Folder already exists.")
    exit()

shutil.copytree("template", f"{day_number}")
