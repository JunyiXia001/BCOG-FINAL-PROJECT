from land import land
from player import player
import random
import tkinter as tk
from PIL import Image, ImageTk
import json
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
        self.info_display_width = 350
        self.info_panel = tk.Frame(self.root, wid=self.info_display_width)
        self.info_panel.grid(row=0, column=1)
        #Map
        self.map_frame = tk.Frame(self.root, height=self.screen_size[1] - self.interface_height)
        self.map_frame.grid(row=0, column=0)
        self.create_map_frame()
        self.create_interface_frame()
        self.create_information_panel()
    
    
    def create_interface_frame(self):
        roll_dice = tk.Button(self.interface_frame, text="Go", command=self.take_turn(), bg="green")
        roll_dice.pack(side = "right",padx=10, pady=10)
        build_button = tk.Button(self.interface_frame, text="Build", command=None, bg="blue") #Need add command to build parts
        build_button.pack(side = "left",padx=10, pady=10)
        sell_button = tk.Button(self.interface_frame, text="Sell", command=None, bg="red") #Need add command to sell part
        sell_button.pack(side = "right",padx=10,pady=10)

    def create_map_frame(self):
        self.map_canvas = tk.Canvas(self.map_frame, width=self.screen_size[0] - self.info_display_width, height = self.screen_size[1] - self.interface_height)
        self.map_canvas.pack(fill="both", expand=True)
        map_img = ImageTk.PhotoImage(Image.open("monopoly.png")) #Need to find a map image
        self.map_canvas.create_image(785,490, image=map_img, anchor=tk.CENTER)

    def create_information_panel(self):









def main():
    #added this line to run the window 
    my_display = Display()
    my_display.root.mainloop()
    player_num = int(input("how many players in this game\n"))
    player_list = []
    for i in range(player_num):
        player_list.append(player(i+1))
    while player_list:
        take_turn()

def roll_die():

    return random.randint(1, 6)

def take_turn(player):
    move = roll_die()

def load_map():
    pass
##load map has been included in the display class 

def paid(player, num):
    if player.money >= num:
        player.money -= num
        return False
    while player.lands:
        sell_land(player)
        if player.money >= tmp_money:
            player.money -= num
            return False
    return True
        
def sell_land(player):
    sell_id = int(input("which to sell\n"))
    while lands[sell_id].level > 0:
        degrade = bool(input("sell the house?"))
        if degrade:
            lands[sell_id].level -= 1
            player.money += lands[sell_id].house_price/2
        else:
            return
    player.lands[sell_id].owner = 0
    player.money += lands[sell_id].mortage


## chance situation
def take_chance():
    with open("take_chance.json") as file_handle:
        chance_card = file_handle.read()
    card_dict = json.loads(chance_card)
    num = random.randint(0,10)
    return card_dict.get(num)


if __name__ == "__main__":
    main()
