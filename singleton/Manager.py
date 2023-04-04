from AgencyManager import AgencyManager, RealEstate

agency_manager = AgencyManager.get_instance()

agency_manager.add_real_estate(RealEstate("str. Bucuresti 49", 122, 149000))
agency_manager.add_real_estate(RealEstate("str. Stefan cel Mare 55", 67, 102500))
agency_manager.add_real_estate(RealEstate("str. Liviu Deleanu 13", 87, 89000))

str_bucuresti = agency_manager.get_real_estate("str. Bucuresti 49")
agency_manager.remove_real_estate(str_bucuresti)

print("informatii bunuri imobile:")
for data in agency_manager.data:
    print(data.address, data.surface, data.price)
