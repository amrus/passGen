# password generator
import string
import random
#dictionaries
chars = 'abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOQRSTUVWXYZ1234567890!@#$%&*'

def passwordGen():
    num = int(input("Enter the number of passwords: "))
    passwordLen = int(input("Enter the desired length of you password: "))
    for p in range(num):
        password = ''
        for c in range(passwordLen):
            password += random.choice(chars)
        print(password)
passwordGen()
