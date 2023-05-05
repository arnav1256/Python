start = int(input('Enter a number (preferably above 295,147,905,179,352,825,856): '))
current = start
print(current)
while current != 1:
    if current % 2 == 0:
        current //= 2
    else:
        current *= 3
        current += 1
        current //= 2
    print(current)
