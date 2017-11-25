from time import sleep
from sys import stdout

# All classes used to model certain aspects of game
# Story (text file) is converted into objects to be used in game

class Location:

    def __init__(self, name, description, destinations):
        self._name = name
        self._description = description
        self._destinations = destinations

    def __str__(self):
        return "%s\n%s" % (self._name, self._description)

    def output(self):
        text = str(self)
        for c in text:
            stdout.write(c)
            stdout.flush()
            sleep(0.02)
        print()


if __name__ == "__main__":
    print("Models/Classes for game.py")
