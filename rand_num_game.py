#Random Number Guess Game by Brandon Dols

# import random functions
from random import seed
from random import choice
from random import shuffle

#main function
def main ():
    # seed random number generator
    seed(1)
    # prepare a sequence
    sequence = [i + 1 for i in range(20)]
    play = True;
    while play:
        shuffle(sequence)
        # make choices from the sequence
        for _ in range(1):
            selection = choice(sequence)
        print('Guess a number from 1 to 20')
        guess = 0
        while int(guess) != selection:
            guess = input('Guess: ')
            # test for proper input
            while guess.isnumeric() == False:
                print('Guess a number from 1 to 20')
                guess = input('Guess: ')
            # guess is too high
            if int(guess) > selection:
                print('Too High')
            # guess is too low
            elif int(guess) < selection:
                print('Too Low')
            # guess is correct
            else:
                print('You guessed correctly!\n')
        # play again menu
        while True:
            play_again = input('Would you like to play again? (y/n)')
            if play_again.upper() == 'N':
                return
            elif play_again.upper() == 'Y':
                break

main()
