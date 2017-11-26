from time import sleep
from sys import stdout

# All classes used to model certain aspects of game
# Story (text files) are converted into objects to be used in game

class Base:

    def __init__(self, name, description):
        self._name = name
        self._description = description

class Location(Base):

    def __init__(self, name, description, items, destinations):
        super().__init__(name, description)
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

    def item_exists(self, item):
        return True if item in self._items else False

    def remove_item(self, item):
        self._items.remove(item)

    def add_item(self, item):
        self._items.append(item)

    def get_destination(self, direction):
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


class Player:

    def __init__(self, location):
        self.xp = 0
        self.level = 0
        self._location = location
        self._inventory = []

    def move(self, new_location):
        self._location = new_location

    def has_item(self, item):
        return True if item in self._inventory else False

    def pickup(self, item):
        self._inventory.append(item)

    def drop(self, item):
        self._inventory.remove(item)

    @property
    def location(self):
        return self._location

    def __str__(self):
        return "XP: {xp}\nLEVEL: {lvl}\nINVENTORY: {items}".format(
                    xp=self.xp, lvl=self.level, items=', '.join(self._inventory)
                )


class Object(Base):

    def __init__(self, name, description, oyield, attributes):
        super().__init__(name, description)
        self._yield = oyield
        self._attributes = attributes


class Tool(Base):

    def __init__(self, name, description, attributes):
        super().__init__(name, description)
        self._attributes = attributes


if __name__ == "__main__":
    print("Models/Classes for game.py")
