from re import match, finditer
from models import Location, Destination

locations = {}

def match_items(pattern, line):
    obj = match(pattern, line)
    if obj: value = line[len(pattern)+1:len(line)-1]
    return (obj, value) if obj else (obj, None)

def initilise_locations(file_name):
    f = open(file_name, 'r')
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


if __name__ == "__main__":
    print("Auxillary methods for game.py")
