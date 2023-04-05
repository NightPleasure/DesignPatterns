from abc import ABC, abstractmethod

class Property(ABC):
    @abstractmethod
    def get_description(self):
        pass

class House(Property):
    def get_description(self):
        return "This is a beautiful house."

class Apartment(Property):
    def get_description(self):
        return "This is a cozy apartment."

class PropertyFactory(ABC):
    @abstractmethod
    def create_property(self):
        pass

class HouseFactory(PropertyFactory):
    def create_property(self):
        return House()

class ApartmentFactory(PropertyFactory):
    def create_property(self):
        return Apartment()

if __name__ == "__main__":
    house_factory = HouseFactory()
    house = house_factory.create_property()
    print(house.get_description())

    apartment_factory = ApartmentFactory()
    apartment = apartment_factory.create_property()
    print(apartment.get_description())
