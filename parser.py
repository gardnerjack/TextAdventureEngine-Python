from re import match, finditer
from models import Location, Destination, Object, Tool

locations = {}
items = {}

def initilise_game_info():
    initilise_locations()
    initialise_items()

def match_items(pattern, line):
    obj = match(pattern, line)
    if obj: value = line[len(pattern)+1:len(line)-1]
    return (obj, value) if obj else (obj, None)

def initilise_locations():
    f = open("game_info/locations.txt", 'r')
    nameObj, descriptionObj, itemsObj, destinationsObj = None, None, None, None
    name, description, items, destinations = None, None, None, None
    for line in f:
        if not nameObj: nameObj, name = match_items("name:", line)
        if not descriptionObj: descriptionObj, description = match_items("description:", line)
        if not itemsObj:
            itemsObj = match("items:", line)
            if itemsObj: items = line[7:len(line)-1].split(', ')
        if not destinationsObj:
            destinationsObj = match("destinations:", line)
            if destinationsObj:
                destinations = []
                for i in finditer(r"\"(.+?)\"\[(.+?)\]", line[14:len(line)-1]):
                    destinations.append(Destination(i.group(1), i.group(2)))
        if match("--", line):
            locations[name] = Location(name, description, items, destinations)
            nameObj, descriptionObj, itemsObj, destinationsObj = None, None, None, None
            name, description, items, destinations = None, None, None, None
    f.close()

def initialise_items():
    f = open("game_info/items.txt", 'r')
    nameObj, typeObj, descriptionObj, attributesObj, yieldObj = None, None, None, None, None
    name, itype, description, attributes, oyield = None, None, None, None, None
    for line in f:
        if not nameObj: nameObj, name = match_items("name:", line)
        if not typeObj: typeObj, itype = match_items("type:", line)
        if not descriptionObj: descriptionObj, description = match_items("description:", line)
        if not yieldObj: yieldObj, oyield = match_items("yield:", line)
        if not attributesObj:
            attributesObj = match("attributes:", line)
            if attributesObj: attributes = line[7:len(line)-1].split(', ')
        if match("--", line):
            if itype == 'object': items[name] = Object(name, description, oyield, attributes)
            elif itype == 'tool': items[name] = Tool(name, description, attributes)
            nameObj, typeObj, descriptionObj, attributesObj, yieldObj = None, None, None, None, None
            name, itype, description, attributes, oyield = None, None, None, None, None
    f.close()


if __name__ == "__main__":
    print("Auxillary methods for game.py")
