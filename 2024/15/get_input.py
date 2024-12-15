import requests
import os
import datetime

# Get the day number
date = datetime.datetime.now().day
day = int(os.getcwd().split("/")[-1])
year = os.getcwd().split("/")[-2]
if date != day and day is not None:
    print(f"Today is not day {day}, it is day {date}.")
    x = input("Continue? (y/n)")
    if x != "y":
        exit()
else:
    day = date

overwrite = True
input_file = "input.txt"
cookie = "53616c7465645f5fd9c524ce69ca731f6ab6e310fa4419ad53ca11fbe3466660f0121bb1e9a686562e4c33f31baf687e0e5676487af2d05f465489b03e1f081e"
if not os.path.exists(input_file) or overwrite:
    page = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": cookie}).text

    with open(input_file, "w",encoding="utf-8") as f:
        f.write(page)

cache_file = f"cache_{day}.html"
page = None
cache = False

if not os.path.exists(cache_file):
    page = requests.get(f"https://adventofcode.com/{year}/day/{day}").text
    if cache:
        with open(cache_file, "w") as f:
            f.write(page)
else:
    with open(cache_file, "r") as f:
        page = f.read()

example_start_string = "<pre><code>"
example_end_string = "</code></pre>"
example_start = page.find(example_start_string)

example_end = page.find(example_end_string)
example = page[len(example_start_string) + example_start: example_end]

print(example[:-1])
x = input("Verify...")
with open("example.txt", "w",encoding="utf-8") as f:
    f.write(example[:-1])

print("DAY,YEAR ", day, year)