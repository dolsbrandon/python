# Hangman Game by Brandon Dols

# Main Game Function
def play_game():
    game_over = False
    word = 'MYSTERY'
    used_word = 'MYSTERY'
    bad_guesses = ''
    num_wrong = 0
    hm_index = [27, 38, 40, 42, 52, 54, 65, 67]
    hm_chars = ['0', '/', '|', '\\', '/', '\\', '|', '|']
    unknown_word = '???????'
    word_lines = '\n-------'
    hm_graphic_empty = '___________\n |        ||\n |        ||\n          ||\n          ||\n          ||\n         /||\ \n        //||\\\ '

    print(hm_graphic_empty)
    print(unknown_word)
    while not (game_over):
        guess = input("Enter your guess: ")
        guess = guess[0].upper()

        if guess in used_word:
            index = used_word.index(guess)
            char = used_word[used_word.index(guess)]
            unknown_word = unknown_word[:index] + char + unknown_word[index + 1:]
            used_word = used_word[:index] + '%' + used_word[index + 1:]
            print(unknown_word[word.index(guess)])
            print(hm_graphic_empty)
            print(unknown_word + word_lines)
            if unknown_word == word:
                print("You found all the letters! You win!")
                game_over = True
                return
            print('You found a letter')
            continue
        elif guess in word:
            print(hm_graphic_empty)
            print(unknown_word + word_lines)
            print('You already found that letter. Try again')
            continue
        elif guess in bad_guesses:
            print(hm_graphic_empty)
            print(unknown_word + word_lines)
            print('You already tried that letter. Try again')
            continue
        else:
            index = hm_index[num_wrong]
            char = hm_chars[num_wrong]
            num_wrong += 1
            hm_graphic_empty = hm_graphic_empty[:index] + char + hm_graphic_empty[index + 1:]
            print(hm_graphic_empty)
            print(unknown_word + word_lines)
            if num_wrong == 8:
                print('Sorry. You lost the game')
                game_over = True
                return unknown_word
            print('Sorry you guessed wrong')
            bad_guesses += guess
            continue

# Initial Welcome Screen Display
print('___________          ')
print(' |        ||    W     H    ')
print(' |0       ||    E     A    ')
print('/ | \     ||    L  T  N    ')
print(' / \      ||    C  O  G    ')
print(' | |      ||    O     M    ')
print('         /||\   M     A    ')
print('        //||\\\  E     N   ')

# While Loop for Main Menu
play = ''
while play != 'y':
    play = input('\nAre you ready to play? (y/n)').upper()
    if play == 'Y':
        play_game()
    elif play == "N":
        break
    else:
        continue