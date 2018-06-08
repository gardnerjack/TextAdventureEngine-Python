class Player(object):

    def __init__(self, location):
        # self.xp = 0
        # self.level = 0
        self._location = location
        self._inventory = []

    def move(self, new_location):
        self._location = new_location

    def has_object(self, obj):
        return True if obj in self._inventory else False

    def pickup(self, obj):
        self._inventory.append(obj)
        print("You pick up:", str(obj))

    def drop(self, obj):
        self._inventory.remove(obj)
        print("You drop:", str(obj))

    @property
    def location(self):
        return self._location

    def __str__(self):
        return "INVENTORY: {objects}".format(
            objects = ', '.join([str(i) for i in self._inventory])
        )
        # return "XP: {xp}\nLEVEL: {lvl}\nINVENTORY: {objects}".format(
        #     xp = self.xp,
        #     lvl = self.level,
        #     objects = ', '.join([str(i) for i in self._inventory])
        # )


if __name__ == "__main__":
    print("Character classes for game.py")
