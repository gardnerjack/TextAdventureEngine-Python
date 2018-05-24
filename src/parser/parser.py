from re import match, finditer
from models.items import Object, Tool
from models.locations import Location, Destination

locations = {}
items = {}

def initilise_game_info():
    initialise_items()
    initilise_locations()

def match_item(pattern, line):
    obj = match(pattern, line)
    if obj is not None:
        value = line[len(pattern) + 1 : len(line) - 1]
    else:
        value = None
    return value

def match_list(pattern, line):
    obj = match(pattern, line)
    if obj is not None:
        items = line[len(pattern) + 1 : len(line) - 1].split(', ')
    else:
        items = None
    return items


def initilise_locations():
    f = open("game_info/locations.txt", 'r')
    name, description, loc_items, destinations = (None,) * 4

    for line in f:

        if name is None:
            name = match_item("name:", line)

        if description is None:
            description = match_item("description:", line)

        if loc_items is None:
            loc_items = match_list("items:", line)

        if destinations is None:
            destinationsObj = match("destinations:", line)
            if destinationsObj is not None:
                destinations = [
                    Destination(dest.group(1), dest.group(2))
                    for dest
                    in finditer(r"\"(.+?)\"\[(.+?)\]", line[14 : len(line) - 1])
                ]

        if match("--", line):
            items_list = [items[i] for i in loc_items] if loc_items else None
            locations[name] = Location(name, description, items_list, destinations)
            name, description, loc_items, destinations = (None,) * 4

    f.close()


def initialise_items():
    f = open("game_info/items.txt", 'r')
    name, item_type, description, attributes, object_yield = (None,) * 5

    for line in f:

        if name is None:
            name = match_item("name:", line)

        if item_type is None:
            item_type = match_item("type:", line)

        if description is None:
            description = match_item("description:", line)

        if object_yield is None:
            object_yield = match_item("yield:", line)

        if attributes is None:
            attributes = match_list("attributes", line)

        if match("--", line):
            if item_type == 'object':
                items[name] = Object(name, description, oyield, attributes)
            elif itemtype == 'tool':
                items[name] = Tool(name, description, attributes)
            name, itype, description, attributes, oyield = (None,) * 5

    f.close()


if __name__ == "__main__":
    print("Initialisation functions for game.py")
