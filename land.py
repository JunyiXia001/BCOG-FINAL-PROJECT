class Land:
    owner = 0
    level = 0
    pledge = False
    def __init__(self, name, land_type, house_price = 0, color = "", price = 0, rent = []):
        self.name = name
        self.land_type = land_type
        self.price = price
        self.rent = rent
        self.house_price = house_price
        self.color = color

    def rentNum(self, die=None):
        if die is None:
            return self.rent[self.level]
        if self.level == 0:
            return die * 4
        else:
            return die * 10

    def __str__(self):
        return self.name
    