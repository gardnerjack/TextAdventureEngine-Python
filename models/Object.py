from abc import ABC

class AbstractObject(ABC):

    def __init__(self, name, description, attributes):
        self._name = name
        self._description = description
        self._attributes = attributes if attributes else []

    def __str__(self):
        return self._name

    def attributes_set(self):
        return set(self._attributes)

    @property
    def description(self):
        return self._description


class Item(AbstractObject):

    def __init__(self, name, description, attributes, item_yield):
        super().__init__(name, description, attributes)
        self._yield = item_yield

    @property
    def reward(self):
        return self._yield


class Tool(AbstractObject):

    def __init__(self, name, description, attributes):
        super().__init__(name, description, attributes)


if __name__ == "__main__":
    print("Models for game.py")
