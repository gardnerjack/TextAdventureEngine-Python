from parser import initilise_locations, locations

def get_input():
    inputted = input('> ')
    return False if inputted in ('q', 'quit') else inputted

def game():
    print()
    for i in locations.values():
        i.info()
        print()


if __name__ == "__main__":
    initilise_locations("StoryA.txt")
    game()
