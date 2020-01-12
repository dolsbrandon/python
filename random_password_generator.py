# Random Password Generator by Brandon Dols

import random
import string
from datetime import datetime

def main():

    # ask user for password length and strength
    p_length = ''
    p_strength = ''
    while not p_length.isnumeric() or int(p_length) < 6 or int(p_length) > 15:
        p_length = input('Choose password length(6-15 characters): ')
    while not p_strength.isnumeric() or int(p_strength) < 1 or int(p_strength) > 4:
        p_strength = input('Choose password strength(1:Very Strong, 2: Strong, 3: Weak, 4: Very Weak): ')

    # random seed using time
    random.seed(datetime.now())

    # password generator function
    passwordGenerator(int(p_length), int(p_strength))

    # main menu
    mainMenu()

def mainMenu():
    while True:
        gen_again = input('Would you like to generate a new password(y/n)? ')
        if gen_again.upper() == 'N':
            return 0
        elif gen_again.upper() == 'Y':
            main()
        else:
            continue

def passwordGenerator(length = 6, strength = 4):
    # set possible password characters
    if strength == 4:
        password = ''
        p_chars_list = string.ascii_lowercase
    elif strength == 3:
        length -= 1
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        p_chars_list = string.ascii_lowercase + string.ascii_uppercase
    elif strength == 2:
        length -= 2
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        p_chars_list = string.ascii_lowercase + string.ascii_uppercase + string.digits
    else:
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        length -= 3
        p_chars_list = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


    # randomize password char list
    c_list = list(p_chars_list)
    random.shuffle(c_list)
    p_chars_list = ''.join(c_list)

    # choose password characters
    for _ in range(length):
        password += random.choice(p_chars_list)

    # randomize password character order
    p_word = list(password)
    random.shuffle(p_word)
    password = ''.join(p_word)
    print(password)

main()
