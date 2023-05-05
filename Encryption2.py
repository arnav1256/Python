import random
result = ''
choice = ''
characters_in_order = [chr(x) for x in range(32, 127)]
while choice != '0':
    choice = input("Do you want to encrypt or decrypt the message?\n1 to encrypt, 2 to decrypt or 0 to exit program. ")
    if choice == '1': #encryption
        message = input('Enter message for encryption: ')
        random.seed(input('Enter an integer to use as an encryption key: '))
        shuffled_list = [chr(x) for x in range(32, 127)]
        random.shuffle(shuffled_list)
        for i in range(0, len(message)):
            result += shuffled_list[characters_in_order.index(message[i])]
        print(result + '\n')
        result = ''
    elif choice == '2': #decryption
        message = input('Enter message to decrypt: ')
        r_seed = input('Enter an integer to use as a decryption key (should be the same one used to encrypt): ')
        random.seed(r_seed)
        shuffled_list = [chr(x) for x in range(32, 127)]
        random.shuffle(shuffled_list)
        for i in range(0, len(message)):
            result += characters_in_order[shuffled_list.index(message[i])]
        print(result + '\n')
        result = ''
    elif choice != '0':
        print('You have entered an invalid input, please try again. \n')