class Item(object):

    def __init__(self, name, description, attributes):
        self._name = name
        self._description = description
        self._attributes = attributes if attributes else []

    def attributes_set(self):
        return set(self._attributes)

    def __str__(self):
        return self._name

    @property
    def description(self):
        return self._description


class Object(Item):

    def __init__(self, name, description, oyield, attributes):
        super().__init__(name, description, attributes)
        self._yield = oyield

    @property
    def reward(self):
        return self._yield


class Tool(Item):

    def __init__(self, name, description, attributes):
        super().__init__(name, description, attributes)


if __name__ == "__main__":
    print("Models for game.py")
