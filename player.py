class player:
    color_count = {
        "Railroad": 0,
        "Utility": 0,
        "Purple": 0,
        "Light Blue": 0,
        "Pink": 0,
        "Orange": 0,
        "Red": 0,
        "Yellow": 0,
        "Green": 0,
        "Dark Blue": 0,
    }
    money = 1500
    lands = []
    cards = []
    position = 0
    jail_status = False
    def __init__(self, id):
        self.id = id

    def land_sum(self):
        return sum(land.mortage + (land.level*land.house_price)/2 for land in lands)

    
        