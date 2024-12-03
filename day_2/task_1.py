with open("./input", "r") as file:
    data = file.readlines()

int_data: list[list[int]] = []

for line in data:
    line = line.strip()
    line = line.split()
    line = [int(i) for i in line]
    int_data.append(line)

safe: int = 0
differences: list[int] = []
flag: bool = False

for line in int_data:
    for i in range(1, len(line)):
        if abs(int(line[i]) - int(line[i-1])) > 3 or abs(int(line[i]) - int(line[i-1])) < 1:
            flag = True
            break
        differences.append(int(line[i]) - int(line[i-1]))
    if not flag:
        if all(i > 0 for i in differences) or all(i < 0 for i in differences):
            safe += 1
    flag = False
    differences.clear()

print(safe)       