def momo(func):
    memoized = {}
    def inner(number):
        if number not in memoized:
            memoized[number] = func(number)
        return memoized[number]
    return inner


def fibonacci(n):
    if n <2: return n
    else: return fibonacci(n-1) + fibonacci(n-2)
#[print(fibonacci(i)) for i in range(100)]
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
#[print(fibonacci_iterative(i)) for i in range(100)]

def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n-1)
#[print(factorial(i)) for i in range(100)]
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
#[print(factorial_iterative(i)) for i in range(100)]

def palindrome(word):
    if len(word) <= 1: return True
    else: return word[0] == word[-1] and palindrome(word[1:-1])
#print(palindrome("ssuss"))

def reverse(word):
    if len(word) <= 1: return word
    else: return reverse(word[1:]) + word[0]
print(reverse("hello world"))


