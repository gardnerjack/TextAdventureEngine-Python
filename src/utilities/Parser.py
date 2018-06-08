import os
from os.path import isdir, exists
from re      import match, finditer

from src.models.Object   import Item, Tool
from src.models.Location import Location, Destination


class Parser(object):

    def __init__(self):
        self.locations = {}
        self.objects = {}
        if not isdir("src/game_info"):
            raise Exception("Have you run the game creation script?")
        if not exists("src/game_info/objects.txt"):
            raise Exception("objects.txt does not exist")
        if not exists("src/game_info/locations.txt"):
            raise Exception("locations.txt does not exist")


    def initilise_game_info(self):
        self.initialise_objects()
        self.initilise_locations()
        return self.objects, self.locations


    def match_object(self, pattern, line):
        obj = match(pattern, line)
        if obj is not None:
            value = line[len(pattern) + 1 : len(line) - 1]
        else:
            value = None
        return value


    def match_list(self, pattern, line):
        obj = match(pattern, line)
        if obj is not None:
            objects = line[len(pattern) + 1 : len(line) - 1].split(', ')
        else:
            objects = None
        return objects


    def initialise_objects(self):
        f = open("src/game_info/objects.txt", 'r')
        name, object_type, description, attributes, item_yield = (None,) * 5

        for line in f:

            if name is None:
                name = self.match_object("name:", line)

            if object_type is None:
                object_type = self.match_object("type:", line)

            if description is None:
                description = self.match_object("description:", line)

            if attributes is None:
                attributes = self.match_list("attributes", line)

            if item_yield is None:
                item_yield = self.match_object("yield:", line)

            if match("--", line):
                if object_type == 'item':
                    self.objects[name] = Item(name, description, attributes, item_yield)
                elif object_type == 'tool':
                    self.objects[name] = Tool(name, description, attributes)
                name, object_type, description, attributes, item_yield = (None,) * 5

        f.close()


    def initilise_locations(self):
        f = open("src/game_info/locations.txt", 'r')
        name, description, loc_objects, destinations = (None,) * 4

        for line in f:

            if name is None:
                name = self.match_object("name:", line)

            if description is None:
                description = self.match_object("description:", line)

            if loc_objects is None:
                loc_objects = self.match_list("objects:", line)

            if destinations is None:
                destinationsObj = match("destinations:", line)
                if destinationsObj is not None:
                    destinations = [
                        Destination(dest.group(1), dest.group(2))
                        for dest
                        in finditer(r"\"(.+?)\"\[(.+?)\]", line[14 : len(line) - 1])
                    ]

            if match("--", line):
                objects_list = [self.objects[i] for i in loc_objects] if loc_objects else None
                self.locations[name] = Location(name, description, objects_list, destinations)
                name, description, loc_objects, destinations = (None,) * 4

        f.close()



if __name__ == "__main__":
    print("Parser for Text Adventure Engine - Reads in game information")
