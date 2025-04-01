from land import Land
from player import player
import random
import tkinter as tk
from PIL import Image, ImageTk
import json
color_num = {
    "Railroad": 4,
    "Purple": 2,
    "Light Blue": 3,
    "Pink": 3,
    "Orange": 3,
    "Red": 3,
    "Yellow": 3,
    "Green": 3,
    "Dark Blue": 2,
    "Utility": 2
}
### MainFrame and Map display 
class Display:
    screen_size = (1920, 1080)
    def __init__(self):
        self.root = tk.Tk()
        self.init_window()
    def init_window(self):
        self.root.title("Monopoly Game")
        #Interface
        self.interface_height = 100
        self.interface_frame = tk.Frame(self.root, height= self.interface_height)
        self.interface_frame.grid(row=1, column=0, columnspan=2)
        #info display
        self.info_display_width = 550
        self.info_panel = tk.Frame(self.root, wid=self.info_display_width)
        self.info_panel.grid(row=0, column=1)
        #Map
        self.map_frame = tk.Frame(self.root, height=self.screen_size[1] - self.interface_height)
        self.map_frame.grid(row=0, column=0)
        self.create_map_frame()
        self.create_interface_frame()
        self.create_information_panel()
    
    
    def create_interface_frame(self):
        roll_dice = tk.Button(self.interface_frame, text="Go", command=None, bg="green") # Need add command of take turn 
        roll_dice.pack(side = "right",padx=10, pady=10)
        build_button = tk.Button(self.interface_frame, text="Build", command=None, bg="yellow") #Need add command to build parts
        build_button.pack(side = "left",padx=10, pady=10)
        sell_button = tk.Button(self.interface_frame, text="Sell", command=None, bg="red") #Need add command to sell part
        sell_button.pack(side = "right",padx=10,pady=10)

    def create_map_frame(self):
        self.map_width = self.screen_size[0] - self.info_display_width
        self.map_height = self.screen_size[1] - self.interface_height
        self.map_canvas = tk.Canvas(self.map_frame, width=self.map_width, height =self.map_height)
        self.map_canvas.pack(fill="both", expand=True)
        self.org_img = Image.open("monopoly.png") #Need to find a map image
        self.rev_img = self.org_img.resize((self.screen_size[0] - self.info_display_width,self.screen_size[1] - self.interface_height), Image.Resampling.LANCZOS)
        self.map_img = ImageTk.PhotoImage(self.rev_img)
        self.map_canvas.create_image(self.map_width // 2,self.map_height // 2, image=self.map_img, anchor=tk.CENTER)

    def create_information_panel(self):
        panel = tk.Label(self.info_panel, text="Game Information", font=("Times New Roman", 12, "bold"))
        panel.pack(pady=(5,5))
        panel_frame = tk.Frame(self.info_panel)
        panel_frame.pack(fill="both", expand=True, padx=10, pady=5)
        scrollbar = tk.Scrollbar(panel_frame)
        scrollbar.pack(side="right", fill="y")
        









def main():
    #added this line to run the window 
    my_display = Display()
    my_display.root.mainloop()
    game_map = loadMap()
    player_num = 2
    player_list = []
    for i in range(player_num):
        player_list.append(player(i+1))
    while len(player_list) > 1:
        takeTurn(game_map, player_list, player[0], 0)
        player.append(player[0])
        player.pop(0)

def rollDie():
    return random.randint(1, 6)

def takeTurn(game_map, player_list, player, count):
    if player.jail_status > 0:
        player.jail_status -= 1
        choice = int(input("paid, roll, card"))
        if choice == 0:
            player.jail_status = 0
            player.money -= 50
        elif choice == 1:
            die1 = rollDie()
            die2 = rollDie()
            if die1 != die2:
                return
            else:
                player.jail_status = 0
    die1 = rollDie()
    die2 = rollDie()
    one_more = False
    
    if die1 == die2:
        count+=1
        one_more = True
    player.position = (player.position + die1 + die2) % 40

    if game_map[player.position].land_type == "Property":
        if game_map[player.position].pledge == False:
            if game_map[player.position].owner == 0:
                buy = bool(input("do you want to buy the land?\n"))
                if buy:
                    buyLand(player, game_map[player.position])
            elif game_map[player.position].owner != 0 and game_map[player.position].owner != player.id:
                paid(player, player_list[game_map[player.position].owner], game_map[player.position].rentNum())

    elif game_map[player.position].land_type == "Railroad":
        if game_map[player.position].pledge == False:
            if game_map[player.position].owner == 0:
                buy = bool(input("do you want to buy the land?\n"))
                if buy:
                    buyLand(player, game_map[player.position])
            elif game_map[player.position].owner != 0 and game_map[player.position].owner != player.id:
                paid(player, player_list[game_map[player.position].owner], game_map[player.position].rentNum())
    
    elif game_map[player.position].land_type == "Utility":
        if game_map[player.position].pledge == False:
            if game_map[player.position].owner == 0:
                buy = bool(input("do you want to buy the land?\n"))
                if buy:
                    buyLand(player, game_map[player.position])
            elif game_map[player.position].owner != 0 and game_map[player.position].owner != player.id:
                paid(player, player_list[game_map[player.position].owner], game_map[player.position].rentNum(die1 + die2))

    elif game_map[player.position].land_type == "Go":
        player.money += 200
    
    elif game_map[player.position].land_type == "Jail":
        player.position = 10
        player.jail_status = 2

    

def buyLand(player, land):
    if player.money >= land.price:
        player.money -= land.price
        player.lands.append(land)
        land.owner = player.id
        if land.land_type == "Property":
            player.color_count[land.color] += 1
            if player.color_count[land.color] == color_num[land.color]:
                for i in player.lands:
                    if i.color == land.color:
                        i.level = 1
        elif land.land_type == "Railroad":
            player.color_count["Railroad"] += 1
            for i in player.lands:
                if i.land_type == "Railroad":
                    i.level = player.color_count["Railroad"] - 1
        elif land.land_type == "Utility":
            player.color_count["Utility"] += 1
            for i in player.lands:
                if i.land_type == "Utility":
                    i.level = player.color_count["Utility"] - 1

def paid(player, receiver, num):
    if player.money >= num:
        player.money -= num
        receiver.money += num
        return False
    if player.land_sum >= num:
        while player.lands:
            sellLand(player)
            if player.money >= tmp_money:
                player.money -= num
                receiver.money += num
                return False
    return True

def loadMap():
    lands = []
    with open("monopoly_space_info.json", "r") as file:
        land_dict = json.load(file)
    for i in range(len(land_dict)):
        lands.append(Land(land_dict[i]["Name"], land_dict[i]["Type"], land_dict[i]["HousePrice"], land_dict[i]["Color"], land_dict[i]["Price"], land_dict[i]["Rent"]))
    return lands

    

def sellLand(player):
    sell_id = int(input("which to sell\n"))
    while lands[sell_id].level > 0:
        degrade = bool(input("sell the house?"))
        if degrade:
            lands[sell_id].level -= 1
            player.money += lands[sell_id].house_price/2
        else:
            return
    sells = bool(input("sell the land?"))
    if sells:
        player.lands[sell_id].pledge = True
        player.money += int(lands[sell_id].price*0.7)


## chance situation
def take_chance():
    with open("take_chance.json") as file_handle:
        chance_card = file_handle.read()
    card_dict = json.loads(chance_card)
    num = random.randint(0,10)
    return card_dict.get(num)


if __name__ == "__main__":
    main()
