file = open('Day_1.txt', 'r')

elf_calories = 0
max_cal = 0
list_calories = []

for line in file:
    line = line.replace("\n", "")
    if line != "":
        elf_calories += int(line)
    else:
        if elf_calories > max_cal:
            max_cal = elf_calories

        list_calories.append(elf_calories)

        elf_calories = 0

list_calories.sort()
print(max_cal)
print(list_calories[-1] + list_calories[-2] + list_calories[-3])
