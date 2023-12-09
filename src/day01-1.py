with open('input/day01.txt') as file:
    lines = [line.rstrip() for line in file]

sum = 0

for line in lines:
    for character in line:
        if character.isdigit():
            digit1 = character
            break

    for character in line[::-1]:
        if character.isdigit():
            digit2 = character
            break

    number = int(digit1 + digit2)
    sum += number

print(sum)
