from abc import ABC, abstractmethod


class PropertyFactory(ABC):
    @abstractmethod
    def create_property(self, address, num_rooms, num_bathrooms):
        pass


class ApartmentFactory(PropertyFactory):
    def create_property(self, address, num_rooms, num_bathrooms):
        return Apartment(address, num_rooms, num_bathrooms)


class HouseFactory(PropertyFactory):
    def create_property(self, address, num_rooms, num_bathrooms):
        return House(address, num_rooms, num_bathrooms)


class Apartment:
    def __init__(self, address, num_rooms, num_bathrooms):
        self.address = address
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms


class House:
    def __init__(self, address, num_rooms, num_bathrooms):
        self.address = address
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
