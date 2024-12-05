with open("./input", "r") as file:
    data = file.readlines()

total: int = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            if i > 2:
                try:
                    if data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
                        total += 1
                    if data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
                        total += 1
                    if data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
                        total += 1
                except:
                    pass
            
            try:
                if data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S":
                    total += 1
                if data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
                    total += 1
            except:
                pass
            
            if i < len(data) - 3:
                if data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
                    total += 1
                if data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
                    total += 1
                if data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
                    total += 1

print(total)