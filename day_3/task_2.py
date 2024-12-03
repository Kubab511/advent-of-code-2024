import re

with open("./input", "r") as file:
    data = file.read()


pattern = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
matches: list[str] = []
matches_unpacked: list[str] = []
total: int = 0
flag: bool = False

matches.extend(re.findall(pattern, data))

matches_unpacked = [i for sub in matches for i in sub]
matches_unpacked = list(filter(None, matches_unpacked))

for item in matches_unpacked:
    if item == "do()":
        flag = False
    elif item == "don't()":
        flag = True
    else:
        if not flag:
            int_1, int_2 = map(int, item[4:-1].split(","))
            total += int_1 * int_2

print(total)