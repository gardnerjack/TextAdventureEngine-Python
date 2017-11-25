from time import sleep
from sys import stdout

# All classes used to model certain aspects of game
# Story (text file) is converted into objects to be used in game

class Location:

    def __init__(self, name, description, items, destinations):
        self._name = name
        self._description = description
        self._destinations = destinations if destinations else []
        self._items = items if items else []

    def __str__(self):
        return "%s\n%s" % (self._name, self._description)

    def output(self):
        text = str(self)
        for c in text:
            stdout.write(c)
            stdout.flush()
        print()

    def move(self, direction):
        if direction == 'n': direction = 'north'
        elif direction == 'e': direction = 'east'
        elif direction == 's': direction = 'south'
        elif direction == 'w': direction = 'west'
        new_location = None
        for d in self._destinations:
            if d.direction == direction:
                new_location = d.name
        if not new_location: print("Nothing that way!")
        return new_location


    def info(self):
        print("name:", self._name)
        print("description:", self._description)
        print("items:", ', '.join(self._items))
        print("destinations:", ', '.join([str(i) for i in self._destinations]))


class Destination:

    def __init__(self, name, direction):
        self._name = name
        self._direction = direction

    @property
    def name(self): return self._name

    @property
    def direction(self): return self._direction

    def __str__(self):
        return "\"%s\"[%s]" % (self._name, self._direction)


if __name__ == "__main__":
    print("Models/Classes for game.py")
