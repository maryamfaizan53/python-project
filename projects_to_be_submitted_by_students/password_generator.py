import random

print('Welcome to your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890'

number = input('Amount of passwords to generate: ')
number = int(number)
length = input('Input your password length: ')
length = int(length)

print('\nhere are your passwords: ')
for passwords in range(number):
    password = ''
    for c in range(length):
      password += random.choice(chars)
    print(password)