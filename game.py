from parser import initilise_game_info, locations, items
from models import Player

MOVE = 'move'
GET = 'get'
DROP = 'drop'

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
        print("actions:\n   get <item>\n   drop <item>\n   use <item> on <object>")
    elif command == 'show':
        player.location.output()
    elif command in ('n', 'w', 's', 'e', 'north', 'west', 'south', 'east'):
        return MOVE
    elif command in ('p', 'player'): print(str(player))
    elif command.startswith('get'): return GET
    elif command.startswith('drop'): return DROP
    elif command.startswith('use'):
        pass  # TODO: check for valid use of command "use <item> on <object>""
    else: print("Please enter a valid command")

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
        todo = handle(command)
        if todo == MOVE:
            move_player(command)
        elif todo == GET:
            item = command[4:]
            if player.location.item_exists(item):
                print("You pick up:", item)
                player.location.remove_item(item)
                player.pickup(item)
            else:
                print("this item isn't here")
        elif todo == DROP:
            item = command[5:]
            if player.has_item(item):
                print("You drop:", item)
                player.location.add_item(item)
                player.drop(item)
            else:
                print("You don't have this item")



if __name__ == "__main__":
    initilise_game_info()
    for i in locations.values():
        current_location = i
        break
    global player
    player = Player(current_location)
    game()
