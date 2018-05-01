from re import match
from parser.parser import initilise_game_info, locations, items
from models.commands import Handler
from models.items import Object, Tool
from models.characters import Player


def get_input():
    inputted = input('> ')
    return False if inputted in ('q', 'quit') else inputted


def move(direction):
    location_name = player.location.get_destination(direction)
    if location_name:
        player.move(locations[location_name])
        player.location.output()


def get(command):
    item = items[command[4:]] if command[4:] in items else None
    if item and player.location.item_exists(item) and type(item) == Tool:
        player.location.remove_item(item)
        player.pickup(item)
    else:
        print("this item isn't here or can't be picked up")


def drop(command):
    item = items[command[4:]] if command[4:] in items else None
    if item and player.has_item(item):
        player.location.add_item(item)
        player.drop(item)
    else:
        print("You don't have: {item}".format(
            item = item
        ))


def use(command):
    matchObj = match(r"use (\S+) on (\S+)", command)
    if matchObj:
        item_text, thing_text = matchObj.groups()

        item  = items[item_text]  if item_text  in items else None
        thing = items[thing_text] if thing_text in items else None

        if not item or not player.has_item(item):
            print("You do not have: {item}".format(
                item = str(item) if item else item_text
            ))

        elif not thing or not player.location.item_exists(thing):
            print("{item} does not exist".format(
                item = str(thing) if thing else thing_text
            ))

        else:
            if len(item.attributes_set().union(thing.attributes_set())) > 0:
                player.pickup(thing.reward)
                player.location.remove_item(thing)
            else:
                print("{item} cannot be used on {thing}".format(
                    item = item,
                    thing = thing
                ))
    else:
        print("Incorrect usage of command: use <item> on <object>")


def inspect(command):
    item = items[command[8:]] if command[8:] in items else None
    if player.has_item(item) or player.location.item_exists(item):
        print(item.description)
    else:
        print("cannot inspect item")


def game():
    player.location.output()
    does_things = Handler()
    while True:
        command = get_input()
        if not command: break
        todo = does_things.handle(command, player)
        if todo: eval(todo + '(command)')


if __name__ == "__main__":
    initilise_game_info()
    global player
    player = Player(list(locations.values())[0])
    game()
