class player:
    money = 1500
    lands = []
    cards = []
    position = 0
    jail_status = False
    def __init__(self, id):
        self.id = id

    def land_sum(self):
        return sum(land.mortage + (land.level*land.house_price)/2 for land in lands)

    
        