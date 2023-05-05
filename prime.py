# import math
# def prime(n):
#     p = True
#     if n <= 1: return
#     for i in range(2, math.ceil(math.sqrt(n))):
#         if n/i == n//i:
#             p = False
#             break
#     return p
# if __name__ == '__main__':
#     num = int(input())
#     if prime(num) == None:
#         print("Not greater than 1")
#     elif prime(num) == True:
#         print("Is prime")
#     elif prime(num) == False:
#         print("Is not prime")
#     a = input("Enter 1 to repeat or anything else to quit: ")
#     while a == "1":
#         num = int(input())
#         if prime(num) == None:
#             print("Not greater than 1")
#         elif prime(num) == True:
#             print("Is prime")
#         elif prime(num) == False:
#             print("Is not prime")
#         a = input("Enter 1 to repeat or anything else to quit: ")



# from string import ascii_uppercase
# d = dict(zip(ascii_uppercase, [0] * 26))
# e = dict(zip(ascii_uppercase, [0] * 26))
# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")
# for i in word1:
#     d[i] += 1
# for i in word2:
#     e[i] += 1
# p = True
# for i in ascii_uppercase:
#     if d[i] > e[i]:
#         p = False
# print(p)


