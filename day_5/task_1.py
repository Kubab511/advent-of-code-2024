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

for i, line in enumerate(pages):
    if not i in incorrect_lines:
        total += int(line[len(line)//2])

# Ten sam kod co powyżej
# for i in range(len(pages)):
#     if not i in incorrect_lines:
#         total += int(pages[i][len(pages[i])//2])

print(total)