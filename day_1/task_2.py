def read_input(filename: str, list_1: list[int], list_2: list[int]) -> tuple[list[int], list[int]]:
    with open(filename, "r") as file:
        for line in file:
            content = line.split()
            list_1.append(int(content[0]))
            list_2.append(int(content[1]))
    return list_1, list_2

list_1, list_2 = read_input("./input", [], [])
total: int = 0
total_times_in_list_2: int = 0

for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i] == list_2[j]:
            total_times_in_list_2 += 1
    total += list_1[i] * total_times_in_list_2
    total_times_in_list_2 = 0

print(total)