from parser import initilise_locations, locations

MOVE = 'move'
QUIT = 'quit'

def get_input():
    inputted = input('> ')
    return False if inputted in ('q', 'quit') else inputted

def handle(command):
    if command in ('h', 'help'):
        print("Available commands:")
        print("h, help - list commands")
        print("q, quit - quit the game")
        print("north, east, south, west - directions to move in")
        print("n, e, s, w - abbreviated versions of movement commands")
        print("show - show description of current location")
    elif command == 'show':
        current_location.output()
    elif command in ('n', 'w', 's', 'e', 'north', 'west', 'south', 'east'):
        return MOVE
    else:
        print("Please enter a value command")

def game():
    global current_location
    current_location.output()
    while True:
        command = get_input()
        if not command: break
        if handle(command) == MOVE:
            new_location = current_location.move(command)
            if new_location:
                current_location = locations[new_location]
                current_location.output()


if __name__ == "__main__":
    initilise_locations("StoryA.txt")
    for i in locations.values():
        current_location = i
        break
    game()
