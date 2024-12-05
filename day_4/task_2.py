with open("./input", "r") as file:
    data = file.readlines()

total: int = 0

for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if data[i][j] == "A":
                if data[i+1][j+1] == "M" and data[i-1][j-1] == "S":
                    if data[i+1][j-1] == "S" and data[i-1][j+1] == "M":
                        total += 1
                        continue
                    if data[i-1][j+1] == "S" and data[i+1][j-1] == "M":
                        total += 1
                        continue
                if data[i-1][j+1] == "M" and data[i+1][j-1] == "S":
                    if data[i-1][j-1] == "S" and data[i+1][j+1] == "M":
                        total += 1
                        continue
                    if data[i+1][j+1] == "S" and data[i-1][j-1] == "M":
                        total += 1
                        continue
                if data[i+1][j-1] == "M" and data[i-1][j+1] == "S":
                    if data[i-1][j-1] == "M" and data[i+1][j+1] == "S":
                        total += 1
                        continue
                    if data[i+1][j+1] == "S" and data[i-1][j-1] == "M":
                        total += 1
                        continue
                if data[i-1][j-1] == "M" and data[i+1][j+1] == "S":
                    if data[i+1][j-1] == "M" and data[i-1][j+1] == "S":
                        total += 1
                        continue
                    if data[i-1][j+1] == "M" and data[i+1][j-1] == "S":
                        total += 1
                        continue

print(total)