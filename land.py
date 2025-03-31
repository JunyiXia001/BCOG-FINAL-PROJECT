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

    def rentNum(self):
        return rent[level]

    def rentNum(self, die):
        if level == 0:
            return die*4
        else:
            return die*10


    