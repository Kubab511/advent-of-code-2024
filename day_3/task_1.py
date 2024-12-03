import re

with open("./input", "r") as file:
    data = file.read()

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches: list[str] = []
total: int = 0


matches.extend(re.findall(pattern, data))

for item in matches:
    int_1, int_2 = map(int, item[4:-1].split(","))
    total += int_1 * int_2

print(total)