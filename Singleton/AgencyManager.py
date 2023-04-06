class RealEstate:
    def __init__(self, address, surface, price):
        self.address = address
        self.surface = surface
        self.price = price


class AgencyManager:
    _instance = None
    data = []

    @staticmethod
    def get_instance():
        if AgencyManager._instance is None:
            AgencyManager._instance = AgencyManager()
        return AgencyManager._instance

    def add_real_estate(self, real_estate):
        self.data.append(real_estate)

    def remove_real_estate(self, real_estate):
        self.data.remove(real_estate)

    def get_real_estate(self, address):
        for real_estate in self.data:
            if real_estate.address == address:
                return real_estate
        return None
