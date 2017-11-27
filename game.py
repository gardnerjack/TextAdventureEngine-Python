from re import match
from parser import initilise_game_info, locations, items
from models import Player, Object, Tool

MOVE = 'move'
GET = 'get'
DROP = 'drop'
USE = 'use'
INSPECT = 'inspect'

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
        print("actions:\n   get <item>\n   drop <item>\n   use <item> on <object>\ninspect <item/object>")
    elif command == 'show':
        player.location.output()
    elif command in ('n', 'w', 's', 'e', 'north', 'west', 'south', 'east'):
        return MOVE
    elif command in ('p', 'player'): print(str(player))
    elif command.startswith('get '): return GET
    elif command.startswith('drop '): return DROP
    elif command.startswith('use '):
        matchObj = match(r"use (\S+) on (\S+)", command)
        if matchObj: return (USE, matchObj.group(1), matchObj.group(2))
        else: print("Incorrect usage of command: use <item> on <object>")
    elif command.startswith('inspect '): return INSPECT
    else: print("Please enter a valid command")

def move_player(direction):
    location_name = player.location.get_destination(direction)
    if location_name:
        player.move(locations[location_name])
        player.location.output()

def get_action(item):
    if player.location.item_exists(item) and type(items[item]) == Tool:
        player.location.remove_item(item)
        player.pickup(item)
    else:
        print("this item isn't here or can't be picked up")

def drop_action(item):
    if player.has_item(item):
        player.location.add_item(item)
        player.drop(item)
    else:
        print("You don't have:", item)

def use_action(item, thing):
    if not player.has_item(item):
        print("You do not have:", item)
    elif not player.location.item_exists(thing):
        print(thing, "does not exist")
    else:
        itemObj, thingObj = items[item], items[thing]
        if len(itemObj.attributes_set().union(thingObj.attributes_set())) > 0:
            player.pickup(thingObj.reward)
            player.location.remove_item(thing)
        else:
            print("%s cannot be used on %s" % (item, thing))

def inspect_action(item):
    if player.has_item(item) or player.location.item_exists(item):
        print(str(items[item]))
    else:
        print("cannot inspect item")


def game():
    player.location.output()
    while True:
        command = get_input()
        if not command: break
        todo = handle(command)
        if not todo: continue
        if todo == MOVE:
            move_player(command)
        elif todo == GET:
            get_action(command[4:])
        elif todo == DROP:
            drop_action(command[5:])
        elif len(todo) > 1 and todo[0] == USE:
            use_action(todo[1], todo[2])
        elif todo == INSPECT:
            inspect_action(command[8:])


if __name__ == "__main__":
    initilise_game_info()
    for i in locations.values():
        current_location = i
        break
    global player
    player = Player(current_location)
    game()
