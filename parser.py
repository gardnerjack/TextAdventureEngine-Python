from re import match
from models import Location

locations = {}

def initilise_locations(file_name):
    f = open(file_name, 'r')
    nameObj, descriptionObj = None, None
    name, description = None, None
    for line in f:
        if not nameObj:
            nameObj = match("name:", line)
            name = line[6:len(line)-1]
        if not descriptionObj:
            descriptionObj = match("description:", line)
            description = line[13:len(line)-1]
        if nameObj and descriptionObj:
            locations[name] = Location(name, description, [])
            nameObj, descriptionObj = None, None
            name, description = None, None


if __name__ == "__main__":
    print("Auxillary methods for game.py")
