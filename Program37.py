import sys

try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
except:
    print('Invalid input. ')
    sys.exit()

def hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = hcf(num1, num2)
print(hcf)
    