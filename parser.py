from re import match, finditer
from models import Location, Destination, Object, Tool

locations = {}
items = {}

def initilise_game_info():
    initialise_items()
    initilise_locations()

def match_item(pattern, line):
    obj = match(pattern, line)
    if obj: value = line[len(pattern)+1:len(line)-1]
    return value if obj else None

def match_list(pattern, line):
    obj = match(pattern, line)
    if obj: items = line[len(pattern)+1:len(line)-1].split(', ')
    return items if obj else None

def initilise_locations():
    f = open("game_info/locations.txt", 'r')
    name, description, loc_items, destinations = None, None, None, None
    for line in f:
        if not name: name = match_item("name:", line)
        if not description: description = match_item("description:", line)
        if not loc_items: loc_items = match_list("items:", line)
        if not destinations:
            destinationsObj = match("destinations:", line)
            if destinationsObj:
                destinations = []
                for i in finditer(r"\"(.+?)\"\[(.+?)\]", line[14:len(line)-1]):
                    destinations.append(Destination(i.group(1), i.group(2)))
        if match("--", line):
            locations[name] = Location(name, description, [items[i] for i in loc_items] if loc_items else None, destinations)
            name, description, loc_items, destinations = None, None, None, None
    f.close()

def initialise_items():
    f = open("game_info/items.txt", 'r')
    name, itype, description, attributes, oyield = None, None, None, None, None
    for line in f:
        if not name: name = match_item("name:", line)
        if not itype: itype = match_item("type:", line)
        if not description: description = match_item("description:", line)
        if not oyield: oyield = match_item("yield:", line)
        if not attributes: attributes = match_list("attributes", line)
        if match("--", line):
            if itype == 'object': items[name] = Object(name, description, oyield, attributes)
            elif itype == 'tool': items[name] = Tool(name, description, attributes)
            name, itype, description, attributes, oyield = None, None, None, None, None
    f.close()


if __name__ == "__main__":
    print("Auxillary methods for game.py")
