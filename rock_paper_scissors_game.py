# Rock Paper Scissors Game by Brandon Dols

# import random functions
from random import seed
from random import choice
from random import shuffle

# main function
def main ():
    # seed random number generator
    seed(777)
    # prepare a weapon_range from 0 to 2
    weapon_range = [i for i in range(3)]
    # list of weapons
    weapons = ['Rock','Paper','Scissors']
    play = True
    while play:
        shuffle(weapon_range)

        # get comp_choice from weapon_range
        for _ in range(1):
            comp_choice = choice(weapon_range)
        player_choice = input('[1.Rock] [2.Paper] [3.Scissors]\nPick Your Weapon(1/2/3): ')

        # test for proper input
        while player_choice.isnumeric() == False or int(player_choice) < 1 or int(player_choice) > 3:
            player_choice = input('[1.Rock] [2.Paper] [3.Scissors]\nPick Your Weapon: ')
        print('Rock, Paper, Scissors, Shoot!\n')

        # set player_choice to align with list index
        player_choice = int(player_choice) - 1

        # print player weapon vs comp weapon
        print(weapons[player_choice] + ' VS ' + weapons[comp_choice])

        # player_choice is less than comp_choice
        if player_choice < comp_choice:
            # player rock vs comp scissors
            if player_choice == 0 and comp_choice == 2:
                print('You Win')
            else:
                print('Computer Wins')

        # player_choice is more than comp_choice
        elif player_choice > comp_choice:
            # player scissors vs comp rock
            if player_choice == 2 and comp_choice == 0:
                print('Computer Wins')
            else:
                print('You Win')

        # draw game
        else:
            print('Game is a draw')

        # play again menu
        while True:
            play_again = input('\nWould you like to play again? (y/n) ')
            if play_again.upper() == 'N':
                return
            elif play_again.upper() == 'Y':
                print('')
                break

main()
