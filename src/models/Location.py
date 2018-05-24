class Location(object):

    def __init__(self, name, description, items, destinations):
        self._name = name
        self._description = description
        self._destinations = destinations if destinations else []
        self._items = items if items else []

        self._abbreviations = {
            'n': 'north',
            'e': 'east',
            's': 'south',
            'w': 'west'
        }


    def __str__(self):
        return "{name}\n{desc}".format(
            name = self._name,
            desc = self._description
        )


    def output(self):
        print(str(self))


    def item_exists(self, item):
        return True if item in self._items else False


    def remove_item(self, item):
        self._items.remove(item)


    def add_item(self, item):
        self._items.append(item)


    def get_destination(self, direction):

        if direction in self._abbreviations:
            direction = self._abbreviations[direction]

        new_location = None
        for d in self._destinations:
            if d.direction == direction:
                new_location = d.name

        if not new_location:
            print("Nothing that way!")

        return new_location


    def info(self):
        print("name:", self._name)
        print("description:", self._description)
        print("items:", ', '.join(self._items))
        print("destinations:", ', '.join([str(i) for i in self._destinations]))



class Destination(object):

    def __init__(self, name, direction):
        self._name = name
        self._direction = direction

    @property
    def name(self):
        return self._name

    @property
    def direction(self):
        return self._direction

    def __str__(self):
        return "\"{name}\"[{direction}]".format(
            name = self._name,
            direction = self._direction
        )
