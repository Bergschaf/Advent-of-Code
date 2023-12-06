import requests
import os
import datetime

# Get the day number
date = datetime.datetime.now().day
day_number = None
if date != day_number and day_number is not None:
    print(f"Today is not day {day_number}, it is day {date}.")
    x = input("Continue? (y/n)")
    if x != "y":
        exit()
else:
    day_number = date

overwrite = True
input_file = "input.txt"
cookie = "53616c7465645f5f1b07966036555a11490d8df7e05f43f23469a35fb851c9436d4619c6d599d2b0e89e8a95b5d288c5b253db0c0a62f6bdbea6d3159f84446e"
if not os.path.exists(input_file) or overwrite:
    page = requests.get(f"https://adventofcode.com/2023/day/{day_number}/input", cookies={"session": cookie}).text

    with open(input_file, "w") as f:
        f.write(page)

cache_file = f"cache_{day_number}.html"
page = None

if not os.path.exists(cache_file):
    page = requests.get(f"https://adventofcode.com/2023/day/{day_number}").text
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
with open("example.txt", "w") as f:
    f.write(example[:-1])

print("DAY: ", day_number)