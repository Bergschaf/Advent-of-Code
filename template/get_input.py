import requests
import os
cache_file = "cache"
page = None
if not os.path.exists(cache_file):
    page = requests.get("https://adventofcode.com/2023/day/1").text
    with open(cache_file,"w") as f:
        f.write(page)
else:
    with open(cache_file, "r") as f:
        page = f.read()


example_start_string = "<pre><code>"
example_end_string = "</code></pre>"
example_start = page.find(example_start_string)

example_end = page.find(example_end_string)
example = page[len(example_start_string) + example_start: example_end]
print(example_end)