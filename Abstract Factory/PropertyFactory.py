from abc import ABC, abstractmethod


class Property(ABC):
    @abstractmethod
    def get_description(self):
        pass


class House(Property):
    def get_description(self):
        return "Aceasta casa contine 5 dormitoare, 2 blocuri sanitare si terasa"


class Apartment(Property):
    def get_description(self):
        return "Acest apartament are o suprafata de 68 m2, 2 dormitoare si 1 bloc sanitar"


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
