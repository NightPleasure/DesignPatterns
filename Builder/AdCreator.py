class AdCreator:
    def __init__(self):
        self.ad = Ad()

    def set_sector(self, sector):
        self.ad.sector = sector

    def set_category(self, category):
        self.ad.category = category

    def set_area(self, area):
        self.ad.area = area

    def set_bedrooms(self, bedrooms):
        self.ad.bedrooms = bedrooms

    def set_baths(self, baths):
        self.ad.baths = baths

    def get_ad(self):
        return self.ad


class Ad:
    def __init__(self):
        self.sector = None
        self.category = None
        self.area = None
        self.bedrooms = None
        self.baths = None

    def __str__(self):
        return f"Sunt in cautare de o/un {self.category} in sectorul {self.sector},\n\
care detine {self.bedrooms} dormitoare si o suprafata de {self.area} m2.\n\
Pe langa asta sa detina {self.baths} blocuri sanitare!"

