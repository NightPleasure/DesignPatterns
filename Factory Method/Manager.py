from PropertyFactory import ApartmentFactory, HouseFactory

apartment_factory = ApartmentFactory()
apartment = apartment_factory.create_property('Stefan cel Mare 69', 3, 2)

print(f"In baza de date a fost adaugat un apartament de pe adresa '{apartment.address}',\
 cu {apartment.rooms} camere si {apartment.baths} blocuri sanitare")

house_factory = HouseFactory()
house = house_factory.create_property('Alexandru cel Bun 44', 4, 3)

print(f"In baza de date a fost adaugata o casa de pe adresa '{house.address}',\
 cu {house.rooms} camere si {house.baths} blocuri sanitare")
