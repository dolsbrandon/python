# Change counter by Brandon Dols

# Function to find appropriate change
def find_change(change):

    remainder = change
    coins = 0
    coin_type = [0,0,0,0]
    coin_name = ['Quarters: ', 'Dimes: ', 'Nickles: ', 'Pennies: ']

    # Cycle through amount of change remaining and add coins appropriately
    while remainder > 0:
        if (remainder - 25) >= 0:
            coin_type[0] += 1
            remainder -= 25
            coins += 1
        elif (remainder - 10) >= 0:
            coin_type[1] += 1
            remainder -= 10
            coins += 1
        elif (remainder - 5) >= 0:
            coin_type[2] += 1
            remainder -= 5
            coins += 1
        elif (remainder - 1) >= 0:
            coin_type[3] += 1
            remainder -= 1
            coins += 1

    # Keep track of cycle through coin_name
    coin_counter = -1

    # Print each coin name with appropriate count
    for x in coin_type:
        coin_counter += 1
        if x > 0:
            print(coin_name[coin_counter] + str(x))

    print('-----------------')
    # Print appropriately if only 1 coin
    if coins <= 1:
        print('Total of ' + str(coins) + ' coin\n')
    else:
        print('Total of ' + str(coins) + ' coins\n')

# Repeat change counter
while 0 != 1:
    # Check to see if input is numeric
    change = ''
    while not(change.isnumeric()):
        change = input('Enter Change Owed: ')
        if not (change.isnumeric()):
            print("Invalid Entry")

    # Find change count
    find_change(int(change))