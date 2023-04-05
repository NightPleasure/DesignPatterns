import copy


class Property:
    def __init__(self, address, rooms, price):
        self.address = address
        self.rooms = rooms
        self.price = price

    def clone(self):
        return copy.deepcopy(self)
