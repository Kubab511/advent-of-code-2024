with open("./input", "r") as file:
    data = file.read()

order, pages = data.split("\n\n")

pages = pages.splitlines()
pages = [line.split(",") for line in pages]

order = [(x,y) for line in order.splitlines() for x, y in [line.split("|")]]
total = 0

incorrect_lines = []
for pair in order:
    for i, line in enumerate(pages):
        if pair[0] in line and pair[1] in line:
            if line.index(pair[0]) > line.index(pair[1]):
                if i not in incorrect_lines: incorrect_lines.append(i)
            else:
                continue

for pair in order:
    for i, line in enumerate(pages):
        if pair[0] in line and pair[1] in line and i in incorrect_lines:
            index_1 = line.index(pair[0])
            index_2 = line.index(pair[1])
            if line.index(pair[0]) > line.index(pair[1]):
                line[index_1], line[index_2] = line[index_2], line[index_1]
            else:
                continue
                

for i, line in enumerate(pages):
    if i in incorrect_lines:
        total += int(line[(len(line)//2)])

print(total)