from abc import ABC, abstractmethod


class IPropertyFactory(ABC):
    @abstractmethod
    def create_property(self, address, rooms, baths):
        pass


class ApartmentFactory(IPropertyFactory):
    def create_property(self, address, rooms, baths):
        return Apartment(address, rooms, baths)


class HouseFactory(IPropertyFactory):
    def create_property(self, address, rooms, baths):
        return House(address, rooms, baths)


class Apartment:
    def __init__(self, address, rooms, baths):
        self.address = address
        self.rooms = rooms
        self.baths = baths


class House:
    def __init__(self, address, rooms, baths):
        self.address = address
        self.rooms = rooms
        self.baths = baths
