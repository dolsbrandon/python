def addStrings(num1, num2):
    """
    Created by Brandon Dols
    Notes from CodeLeet:

    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

    Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
    """

    # digit conversion dictionary
    digits = {'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'1':1,'0':0}

    # Convert num1 from str to int
    len_num1 = len(num1)
    num1_total = 0
    i = 0
    while i < len(num1):
        for x in num1:
            dec_places = 10 ** (len_num1 - 1)
            if i == len(num1) - 1:
                dec_places = 1
            num1_total += digits[x] * dec_places
            len_num1 -= 1
            i += 1

    # Convert num2 from str to int
    len_num2 = len(num2)
    num2_total = 0
    i = 0
    while i < len(num2):
        for x in num2:
            dec_places = 10 ** (len_num2 - 1)
            if i == len(num2) - 1:
                dec_places = 1
            num2_total += digits[x] * dec_places
            len_num2 -= 1
            i += 1

    # calculate sum
    total = num1_total + num2_total
    print(f'The sum of the two numbers is {total}')

# get user input for numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# send inputs to function
addStrings(num1,num2)