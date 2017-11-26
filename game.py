from parser import initilise_locations, locations
from models import Player

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
        print("p, player - display player information")
    elif command == 'show':
        current_location.output()
    elif command in ('n', 'w', 's', 'e', 'north', 'west', 'south', 'east'):
        return MOVE
    else:
        print("Please enter a value command")

def move_player(direction):
    location_name = player.location.get_destination(direction)
    if location_name:
        player.move(locations[location_name])
        player.location.output()

def game():
    player.location.output()
    while True:
        command = get_input()
        if not command: break
        if handle(command) == MOVE:
            move_player(command)



if __name__ == "__main__":
    initilise_locations("game_info/locations.txt")
    for i in locations.values():
        current_location = i
        break
    global player
    player = Player(current_location)
    game()
