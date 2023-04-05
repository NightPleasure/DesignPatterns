from PropertyFactory import ApartmentFactory, HouseFactory

apartment_factory = ApartmentFactory()
apartment = apartment_factory.create_property('Strada X', 3, 2)

house_factory = HouseFactory()
house = house_factory.create_property('Strada Y', 4, 3)
