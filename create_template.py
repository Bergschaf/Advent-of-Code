import os
import shutil

day = int(input("Day: "))
year = 2021 #  TODO change

if not os.path.exists(f"{year}"):
    os.mkdir(f"{year}")

if os.path.exists(f"{year}/{day}"):
    print("Folder already exists")
    exit()

shutil.copytree("template", f"{year}/{day}")
