import os
import shutil

day = 10
year = 2024

if not os.path.exists(f"{year}"):
    os.mkdir(f"{year}")

if os.path.exists(f"{year}/{day}"):
    print("Folder already exists")
    exit()

shutil.copytree("template", f"{year}/{day}")
