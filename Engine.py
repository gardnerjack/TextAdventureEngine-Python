from re import match

from utilities.Parser  import Parser
from utilities.Handler import Handler
from models.Object     import Item, Tool
from models.Player     import Player


class Engine(object):

    def __init__(self):
        self.objects, self.locations = Parser().initilise_game_info()
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
        obj = self.objects.get(command[4:])
        if obj and self.player.location.object_exists(obj) and isinstance(obj, Tool):
            self.player.location.remove_object(obj)
            self.player.pickup(obj)
        else:
            print("This object isn't here or can't be picked up")


    def drop(self, command):
        obj = self.objects.get(command[4:])
        if obj and self.player.has_object(obj):
            self.player.location.add_object(obj)
            self.player.drop(obj)
        else:
            print("You don't have: {obj}".format(
                obj = obj
            ))


    def use(self, command):
        matchObj = match(r"use (\S+) on (\S+)", command)
        if matchObj:
            tool_text, item_text = matchObj.groups()

            tool = self.objects.get(tool_text)
            item = self.objects.get(item_text)

            if not tool or not self.player.has_object(tool):
                print("You do not have: {tool}".format(
                    tool = tool_text
                ))

            elif not item or not self.player.location.object_exists(item):
                print("{item} does not exist".format(
                    item = item_text
                ))

            else:
                is_tool = isinstance(tool, Tool)
                is_item = isinstance(item, Item)
                if is_tool and is_item and len(tool.attributes_set().union(item.attributes_set())) > 0:
                    self.player.pickup(item.reward)
                    self.player.location.remove_object(item)
                else:
                    print("{tool} cannot be used on {item}".format(
                        tool = tool,
                        item = item
                    ))
        else:
            print("Incorrect usage of command: use <tool> on <item>")


    def inspect(self, command):
        obj = self.objects.get(command[8:])
        if self.player.has_object(obj) or self.player.location.object_exists(obj):
            print(obj.description)
        else:
            print("cannot inspect object")


    def play(self):
        self.player.location.output()
        while True:
            command = self.get_input()
            if not command:
                break
            todo = self.handler.handle(command, self.player)
            if todo:
                eval('self.' + todo + '(command)')
