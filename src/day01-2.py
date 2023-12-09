def get_digit(line, index):
    if line[index] == '0' or line.startswith("zero", index):
        return 0
    if line[index] == '1' or line.startswith("one", index):
        return 1
    if line[index] == '2' or line.startswith("two", index):
        return 2
    if line[index] == '3' or line.startswith("three", index):
        return 3
    if line[index] == '4' or line.startswith("four", index):
        return 4
    if line[index] == '5' or line.startswith("five", index):
        return 5
    if line[index] == '6' or line.startswith("six", index):
        return 6
    if line[index] == '7' or line.startswith("seven", index):
        return 7
    if line[index] == '8' or line.startswith("eight", index):
        return 8
    if line[index] == '9' or line.startswith("nine", index):
        return 9
    return None


with open('input/day01.txt') as file:
    lines = [line.rstrip() for line in file]

sum = 0

for line in lines:
    for index in range(len(line)):
        digit1 = get_digit(line, index)
        if digit1 is not None:
            break

    for index in range(len(line) - 1, -1, -1):
        digit2 = get_digit(line, index)
        if digit2 is not None:
            break

    number = 10 * digit1 + digit2
    sum += number

print(sum)