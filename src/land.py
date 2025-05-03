class Land:
    def __init__(self, name, land_type, house_price = 0, color = "", price = 0, rent = [], location = None):
        self.owner = 0
        self.level = 0
        self.pledge = False
        self.name = name
        self.land_type = land_type
        self.price = price
        self.rent = rent
        self.house_price = house_price
        self.color = color
        self.location = location
    def rent_Num(self, die=None):
        if die is None:
            return self.rent[self.level]
        if self.level == 0:
            return die * 4
        else:
            return die * 10

    def __str__(self):
        return self.name
    