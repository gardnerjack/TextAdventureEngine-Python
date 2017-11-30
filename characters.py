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
        print("You pick up:", str(item))

    def drop(self, item):
        self._inventory.remove(item)
        print("You drop:", str(item))

    @property
    def location(self):
        return self._location

    def __str__(self):
        return "XP: {xp}\nLEVEL: {lvl}\nINVENTORY: {items}".format(
                    xp=self.xp, lvl=self.level, items=', '.join([str(i) for i in self._inventory])
                )


if __name__ == "__main__":
    print("Character classes for game.py")
