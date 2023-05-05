re = int(input('Enter the real component: '))
im = int(input('Enter the imaginary component: '))
num = complex(re, im)
print(num)
while True:
    if ((num.real % 2 == 0) and (num.imag % 2 == 0)) or ((num.real % 2 == 1) and (num.imag % 2 == 1)):
        num /= 2
    else:
        num *= 3
        num += 1
    print(num)