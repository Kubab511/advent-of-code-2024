import re

with open("./input", "r") as file:
    data = file.readlines()


pattern = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
matches: list[str] = []
matches_unpacked: list[str] = []
total: int = 0
flag: bool = False

for line in data:
    matches.extend(re.findall(pattern, line))

matches_unpacked = [i for sub in matches for i in sub]
matches_unpacked = list(filter(None, matches_unpacked))

for item in matches_unpacked:
    if item == "do()":
        flag = False
        continue
    elif item == "don't()":
        flag = True
        continue

    if not flag:
        try:
            item = item[4:-1]
            total += int(item.split(",")[0]) * int(item.split(",")[1])
        except:
            pass

print(total)