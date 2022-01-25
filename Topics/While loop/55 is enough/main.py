import statistics

BREAK_NUMBER = 55
run = True
numbers = []

while run:
    number = int(input())
    if number == BREAK_NUMBER:
        run = False
    else:
        numbers.append(number)

print(len(numbers))
print(sum(numbers))
print(round(statistics.mean(numbers)))  # average of numbers
