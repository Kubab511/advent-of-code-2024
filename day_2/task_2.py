with open("./input", "r") as file:
    data = file.readlines()

int_data: list[list[int]] = []

for line in data:
    line = line.strip()
    line = line.split()
    line = [int(i) for i in line]
    int_data.append(line)

def is_safe(line) -> bool:
    flag: bool = False
    differences: list[int] = []
    for i in range(1, len(line)):
        if abs(int(line[i]) - int(line[i-1])) > 3 or abs(int(line[i]) - int(line[i-1])) < 1:
            flag = True
            break
        differences.append(int(line[i]) - int(line[i-1]))
    if not flag:
        if all(i > 0 for i in differences) or all(i < 0 for i in differences):
            return True
    return False

safe: int = 0
differences: list[int] = []
flag: bool = False

for line in int_data:
    if is_safe(line):
        safe += 1
    else:
        length = len(line)
        line_orig = line.copy()
        for i in range(length):
            del line[i]
            if is_safe(line):
                safe += 1
                break
            line = line_orig.copy()
        
print(safe)