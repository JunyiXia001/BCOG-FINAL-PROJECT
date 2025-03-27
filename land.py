class land:
    owner = 0
    level = 0
    buy = True
    pledge = False
    def __init__(self, name, land_type, house_price = 0, color = "", price = 0, mortage = 0, rent = []):
        self.name = name
        self.land_type = land_type
        self.price = price
        self.mortage = mortage
        self.rent = rent
        self.house_price = house_price
        self.color = color
    def paid(self):
        return rent[level]
    