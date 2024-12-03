def read_input(filename: str, list_1: list[int], list_2: list[int]) -> tuple[list[int], list[int]]:
    with open(filename, "r") as file:
        for line in file:
            content = line.split()
            list_1.append(int(content[0]))
            list_2.append(int(content[1]))
    return list_1, list_2

list_1, list_2 = read_input("./input", [], [])

list_1.sort()
list_2.sort()
total_distance: int = 0

for i in range(len(list_1)):
    total_distance += abs(list_1[i] - list_2[i])

print(total_distance)