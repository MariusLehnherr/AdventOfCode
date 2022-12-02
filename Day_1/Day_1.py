file = open('Day_1.txt', 'r')
elf_calories = 0
max_cal = 0
list_calories = []

for line in file:
    newline = line.replace("\n", "")
    if newline != "":
        elf_calories += int(newline)
    else:
        if elf_calories > max_cal:
            max_cal = elf_calories

        list_calories.append(elf_calories)

        elf_calories = 0

list_calories.sort()
print(max_cal)
print(list_calories[-1] + list_calories[-2] + list_calories[-3])
file.close()