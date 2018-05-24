from re import match
from parser.Parser import Parser
from models.Handler import Handler
from models.Item import Object, Tool
from models.Player import Player


class Engine(object):

    def __init__(self):
        self.locations, self.items = Parser().initilise_game_info()
        self.player = Player(list(self.locations.values())[0])
        self.handler = Handler()


    def get_input(self):
        inputted = input('> ')
        return False if inputted in ('q', 'quit') else inputted


    def move(self, direction):
        location_name = self.player.location.get_destination(direction)
        if location_name:
            self.player.move(self.locations[location_name])
            self.player.location.output()


    def get(self, command):
        item = self.items[command[4:]] if command[4:] in self.items else None
        if item and self.player.location.item_exists(item) and type(item) == Tool:
            self.player.location.remove_item(item)
            self.player.pickup(item)
        else:
            print("this item isn't here or can't be picked up")


    def drop(self, command):
        item = self.items[command[4:]] if command[4:] in self.items else None
        if item and self.player.has_item(item):
            self.player.location.add_item(item)
            self.player.drop(item)
        else:
            print("You don't have: {item}".format(
                item = item
            ))


    def use(self, command):
        matchObj = match(r"use (\S+) on (\S+)", command)
        if matchObj:
            item_text, thing_text = matchObj.groups()

            item  = self.items[item_text]  if item_text  in self.items else None
            thing = self.items[thing_text] if thing_text in self.items else None

            if not item or not self.player.has_item(item):
                print("You do not have: {item}".format(
                    item = str(item) if item else item_text
                ))

            elif not thing or not self.player.location.item_exists(thing):
                print("{item} does not exist".format(
                    item = str(thing) if thing else thing_text
                ))

            else:
                if len(item.attributes_set().union(thing.attributes_set())) > 0:
                    self.player.pickup(thing.reward)
                    self.player.location.remove_item(thing)
                else:
                    print("{item} cannot be used on {thing}".format(
                        item = item,
                        thing = thing
                    ))
        else:
            print("Incorrect usage of command: use <item> on <object>")


    def inspect(self, command):
        item = self.items[command[8:]] if command[8:] in self.items else None
        if self.player.has_item(item) or self.player.location.item_exists(item):
            print(item.description)
        else:
            print("cannot inspect item")


    def play(self):
        self.player.location.output()
        while True:
            command = self.get_input()
            if not command: break
            todo = self.handler.handle(command, self.player)
            if todo: eval(todo + '(command)')


if __name__ == "__main__":
    engine = Engine()
    engine.play()
