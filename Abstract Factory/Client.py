from PropertyFactory import HouseFactory, ApartmentFactory

house_factory = HouseFactory()
house = house_factory.create_property()
print(house.get_description())

apartment_factory = ApartmentFactory()
apartment = apartment_factory.create_property()
print(apartment.get_description())