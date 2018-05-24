from re      import match, finditer
import os
from os.path import isdir, exists

from src.models.Item     import Object, Tool
from src.models.Location import Location, Destination


class Parser(object):

    def __init__(self):
        self.locations = {}
        self.items = {}
        if not isdir("src/game_info"):
            raise Exception("Have you run the game creation script?")
        if not exists("src/game_info/items.txt"):
            raise Exception("items.txt does not exist")
        if not exists("src/game_info/locations.txt"):
            raise Exception("locations.txt does not exist")


    def initilise_game_info(self):
        self.initialise_items()
        self.initilise_locations()
        return self.items, self.locations


    def match_item(self, pattern, line):
        obj = match(pattern, line)
        if obj is not None:
            value = line[len(pattern) + 1 : len(line) - 1]
        else:
            value = None
        return value


    def match_list(self, pattern, line):
        obj = match(pattern, line)
        if obj is not None:
            items = line[len(pattern) + 1 : len(line) - 1].split(', ')
        else:
            items = None
        return items


    def initilise_locations(self):
        f = open("src/game_info/locations.txt", 'r')
        name, description, loc_items, destinations = (None,) * 4

        for line in f:

            if name is None:
                name = self.match_item("name:", line)

            if description is None:
                description = self.match_item("description:", line)

            if loc_items is None:
                loc_items = self.match_list("items:", line)

            if destinations is None:
                destinationsObj = match("destinations:", line)
                if destinationsObj is not None:
                    destinations = [
                        Destination(dest.group(1), dest.group(2))
                        for dest
                        in finditer(r"\"(.+?)\"\[(.+?)\]", line[14 : len(line) - 1])
                    ]

            if match("--", line):
                self.items_list = [self.items[i] for i in loc_items] if loc_items else None
                self.locations[name] = Location(name, description, self.items_list, destinations)
                name, description, loc_items, destinations = (None,) * 4

        f.close()


    def initialise_items(self):
        f = open("src/game_info/items.txt", 'r')
        name, item_type, description, attributes, object_yield = (None,) * 5

        for line in f:

            if name is None:
                name = self.match_item("name:", line)

            if item_type is None:
                item_type = self.match_item("type:", line)

            if description is None:
                description = self.match_item("description:", line)

            if object_yield is None:
                object_yield = self.match_item("yield:", line)

            if attributes is None:
                attributes = self.match_list("attributes", line)

            if match("--", line):
                if item_type == 'object':
                    self.items[name] = Object(name, description, object_yield, attributes)
                elif item_type == 'tool':
                    self.items[name] = Tool(name, description, attributes)
                name, item_type, description, attributes, object_yield = (None,) * 5

        f.close()



if __name__ == "__main__":
    print("Parser for Text Adventure Engine - Reads in game information")
