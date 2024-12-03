import re

with open("./input", "r") as file:
    data = file.readlines()

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches: list[str] = []
total: int = 0

for line in data:
    matches.extend(re.findall(pattern, line))

for item in matches:
    try:
        item = item[4:-1]
        total += int(item.split(",")[0]) * int(item.split(",")[1])
    except:
        pass

print(total)