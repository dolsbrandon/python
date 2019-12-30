# Pyramid maker by Brandon Dols

# Creates pyramid of desired size
def pyramid(height):
    rows = 0
    row_space = height
    while rows < height:
        rows +=1
        row_space -= 1
        print(' '*row_space + '#' * rows + ('#' * (rows-1)))

# Main Menu
def main_menu():
    replay = True
    while replay:
        height = input('How tall do you want your pyramid?')
        if not(height.isnumeric()):
            height = 4
        pyramid(int(height))

# Start Main Menu
main_menu()