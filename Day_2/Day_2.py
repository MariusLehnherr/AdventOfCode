file = open('Day_2.txt', 'r')

total_score = 0
result_of_round = 0
#Task 1
#X = 1   my guess = rock        is A for opponent
#Y = 2   my guess = paper       is B for opponent
#Z = 3   my guess = scissors    is C for opponent

for line in file:
    if line.__contains__("A Y") or line.__contains__("B Z") or line.__contains__("C X"):
        result_of_round = 6
    elif line.__contains__("A X") or line.__contains__("B Y") or line.__contains__("C Z"):
        result_of_round = 3
    else:
        result_of_round = 0

    if line.__contains__("X"):
        result_of_round += 1
    elif line.__contains__("Y"):
        result_of_round += 2
    elif line.__contains__("Z"):
        result_of_round += 3

    total_score += result_of_round

print("Task 1: ")
print(total_score)
total_score = 0
file.close()

#Task 2
file = open('Day_2.txt', 'r')

for lines in file:
    if lines.__contains__("Z"):
        result_of_round = 6
        if lines.__contains__("A"):
            result_of_round += 2
        elif lines.__contains__("B"):
            result_of_round += 3
        else:
            result_of_round += 1

    if lines.__contains__("Y"):
        result_of_round = 3
        if lines.__contains__("A"):
            result_of_round += 1
        elif lines.__contains__("B"):
            result_of_round += 2
        else:
            result_of_round += 3

    if lines.__contains__("X"):
        result_of_round = 0
        if lines.__contains__("A"):
            result_of_round += 3
        elif lines.__contains__("B"):
            result_of_round += 1
        else:
            result_of_round += 2

    total_score += result_of_round

print("Task 2: ")
print(total_score)

file.close()