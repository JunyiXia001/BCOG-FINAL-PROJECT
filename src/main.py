from land import Land
from player import Player
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

##Junyi Xia 
### MainFrame and Map display 
class Display:   
    screen_size = (1280, 720)
    def __init__(self):
        #Basic setup of display function 
        self.root = tk.Tk()
        self.player_num = 2
        self.init_window()
        self.game_map = load_Map()
        self.player_list = [Player(i + 1) for i in range(self.player_num)]  
        self.current_player = self.player_list[0]
        self.land = None

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
        self.map_frame = tk.Frame(self.root, height=self.screen_size[1] - self.interface_height, width=self.screen_size[0] - self.info_display_width)
        self.map_frame.grid(row=0, column=0)
        self.create_map_frame()
        self.create_interface_frame()
        self.buy_button.pack_forget()
        self.End_button.pack_forget()
        self.create_information_panel()
    
    #Create interface frame and buttons 
    def create_interface_frame(self):
        self.take_turn_button = tk.Button(self.interface_frame, text="Go", command=self.call_take_turn, bg="green") 
        self.take_turn_button.pack(side = "right",padx=10, pady=10)
        self.buy_button = tk.Button(self.interface_frame, text="Buy", command=self.call_buy_land, bg="yellow") 
        self.buy_button.pack(side = "left",padx=10, pady=10)
        self.sell_button = tk.Button(self.interface_frame, text="Sell", command=self.call_sell_land, bg="red") 
        self.sell_button.pack(side = "right",padx=10,pady=10)
        self.End_button = tk.Button(self.interface_frame, text="End", command=self.call_end, bg="yellow") 
        self.End_button.pack(side = "right",padx=10,pady=10)

    #Create map frame and load map
    def create_map_frame(self):
        self.map_width = self.screen_size[0] - self.info_display_width
        self.map_height = self.screen_size[1] - self.interface_height
        self.map_canvas = tk.Canvas(self.map_frame, width=self.map_width, height =self.map_height)
        self.map_canvas.pack(fill="both", expand=True)
        self.org_img = Image.open("Image/monopoly.png") 
        self.rev_img = self.org_img.resize(( self.map_width,self.map_height), Image.Resampling.LANCZOS)
        self.map_img = ImageTk.PhotoImage(self.rev_img)
        self.map_canvas.create_image(self.map_width // 2,self.map_height // 2, image=self.map_img, anchor=tk.CENTER)

    #Create information panel 
    def create_information_panel(self):
        panel = tk.Label(self.info_panel, text="Game Information", font=("Times New Roman", 12, "bold"))
        panel.pack(pady=(5,5))
        panel_frame = tk.Frame(self.info_panel)
        panel_frame.pack(fill="both", expand=True, padx=10, pady=5)
        scroll_bar = tk.Scrollbar(panel_frame)
        scroll_bar.pack(side="right", fill="y")
    #Create message box 
        self.info_frame = tk.Text(panel_frame, wrap="word", height=30, width=50, yscrollcommand=scroll_bar.set, state="disabled")
        self.info_frame.pack(side="left", fill="both", expand=True)
        scroll_bar.config(command=self.info_frame.yview)
        self.message("Welcome to Monopoly Game")
        self.message(f"Current player is {self.player_num}. Each player has $1500.")
        self.message("Click Go! to start the game! Good Luck!\n")
    # connect button with take turn method 

    def call_take_turn(self):
        print("Go pressed")
        self.message(f"It's {self.current_player.name}'s turn.")
        self.message(f"money: {self.current_player.money}")
        self.take_turn()
        # self.buy_button.pack_forget()
        self.take_turn_button.pack_forget()
        self.End_button.pack(side = "right",padx=10,pady=10)
        # self.player_list.append(self.player_list.pop(0)) 
        # self.current_player = self.player_list[0]
    # connect button with buy land method 

    def call_buy_land(self):
        print("Buy pressed")
        self.buy_Land()
        self.message(f"this land is now {self.game_map[self.current_player.position].owner}\n")
        self.buy_button.pack_forget()

    def call_sell_land(self):
        sell_Land(self.current_player)
    # setup for message box 
    ## Source from stackoverflow Date: 4/3/2025 Link: https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only?

    def call_end(self):
        self.End_button.pack_forget()
        self.player_list.append(self.player_list.pop(0)) 
        self.current_player = self.player_list[0]
        self.take_turn_button.pack(side = "right",padx=10, pady=10)

    def message(self, message):
        self.info_frame.config(state="normal")
        self.info_frame.insert("end", message + "\n")
        self.info_frame.see("end")
        self.info_frame.config(state="disabled")

    def take_turn(self):
        #Check player's jail status
        
        # if player.jail_status > 0:
        #     player.jail_status -= 1
        #     choice = int(input("paid, roll, wait"))
        #     if choice == 0:
        #         player.jail_status = 0
        #         player.money -= 50
        #     elif choice == 1:
        #         die1 = roll_die()
        #         die2 = roll_die()
        #         if die1 != die2:
        #             return
        #         else:
        #             player.jail_status = 0
        #     elif choice == 3:
        #         return
            
        die1 = roll_die()
        die2 = roll_die()
        one_more = False
        #Move
        if die1 == die2:
            # count+=1
            one_more = True
        if self.current_player.position + die1 + die2 >= 40:
            self.message("pass go, get 200\n")
            self.current_player.money += 200
        #for debug fix moving range
        self.current_player.position = (self.current_player.position + 4) % 40
        land = self.game_map[self.current_player.position]
        self.land
        self.message(f"{self.current_player.name} go to {land.name}.\n")
        # self.current_player.position = (self.current_player.position + die1 + die2) % 40

        # move to jail if continue move for 3 times
        # if count == 3:
        #     self.current_player.position = 10
        #     self.current_player.jail_status = 2

        #Check the space that players move to
        #Property
        if self.game_map[self.current_player.position].land_type == "Property":
            if self.game_map[self.current_player.position].pledge == False:
                if self.game_map[self.current_player.position].owner == 0:
                    self.message("do you want to buy the land?\n")
                    self.buy_button.pack(side = "right",padx=10, pady=10)
                    # buy = bool(input("0: no, 1: yes"))
                    # if buy:
                    #     self.buyLand()
                elif self.game_map[self.current_player.position].owner != 0 and self.game_map[self.current_player.position].owner != self.current_player.id:
                    self.paid(self.current_player.id - 1, self.game_map[self.current_player.position].owner - 1, self.game_map[self.current_player.position].rent_Num())
        #Railroad
        elif self.game_map[self.current_player.position].land_type == "Railroad":
            if self.game_map[self.current_player.position].pledge == False:
                if self.game_map[self.current_player.position].owner == 0:
                    self.message("do you want to buy the land?\n")
                    self.buy_button.pack(side = "right",padx=10, pady=10)
                    # buy = bool(input("0: no, 1: yes"))
                    # if buy:
                    #     self.buyLand()
                elif self.game_map[self.current_player.position].owner != 0 and self.game_map[self.current_player.position].owner != self.current_player.id:
                    self.paid(self.current_player.id - 1, self.game_map[self.current_player.position].owner - 1, self.game_map[self.current_player.position].rent_Num())
        #Utility
        elif self.game_map[self.current_player.position].land_type == "Utility":
            if self.game_map[self.current_player.position].pledge == False:
                if self.game_map[self.current_player.position].owner == 0:
                    self.message("do you want to buy the land?\n")
                    self.buy_button.pack(side = "right",padx=10, pady=10)
                    # buy = bool(input("0: no, 1: yes"))
                    # if buy:
                    #     self.buyLand()
                elif self.game_map[self.current_player.position].owner != 0 and self.game_map[self.current_player.position].owner != self.current_player.id:
                    self.paid(self.current_player.id - 1, self.game_map[self.current_player.position].owner - 1, self.game_map[self.current_player.position].rent_Num(die1 + die2))
        #Jail
        elif self.game_map[self.current_player.position].land_type == "Jail":
            self.current_player.position = 10
            self.current_player.jail_status = 2
        #Income tax
        elif self.game_map[self.current_player.position].land_type == "Income Tax":
            self.paid_bank(200)
        #Luxury Tax
        elif self.game_map[self.current_player.position].land_type == "Luxury Tax":
            self.paid_bank(100)
        #use previous one_more and count to decide whether the player have another moving chance
        
        ##BUG
        # if one_more == True:
        #     take_turn(game_map, player_list, player, count)
        
    def buy_Land(self):
        self.message(f"is {self.current_player.name} buying")
        if self.current_player.money >= self.game_map[self.current_player.position].price:
            self.current_player.money -= self.game_map[self.current_player.position].price
            self.current_player.lands.append(self.game_map[self.current_player.position])
            self.game_map[self.current_player.position].owner = self.current_player.id
            if self.game_map[self.current_player.position].land_type == "Property":
                self.current_player.color_count[self.game_map[self.current_player.position].color] += 1
                if self.current_player.color_count[self.game_map[self.current_player.position].color] == color_num[self.game_map[self.current_player.position].color]:
                    for i in self.current_player.lands:
                        if i.color == self.game_map[self.current_player.position].color:
                            i.level = 1
            elif self.game_map[self.current_player.position].land_type == "Railroad":
                self.current_player.color_count["Railroad"] += 1
                for i in self.current_player.lands:
                    if i.land_type == "Railroad":
                        i.level = self.current_player.color_count["Railroad"] - 1
            elif self.game_map[self.current_player.position].land_type == "Utility":
                self.current_player.color_count["Utility"] += 1
                for i in self.current_player.lands:
                    if i.land_type == "Utility":
                        i.level = self.current_player.color_count["Utility"] - 1

    def paid(self, player, receiver, num):
        self.message(f"{self.player_list[player].name} pay {self.player_list[receiver].name} money by {num}")
        if self.player_list[player].money >= num:
            self.player_list[player].money -= num
            self.player_list[receiver].money += num
            return False
        if self.player_list[player].land_sum >= num:
            while self.player_list[player].lands:
                sell_Land(player)
                if self.player_list[player].money >= tmp_money:
                    self.player_list[player].money -= num
                    self.player_list[receiver].money += num
                    return False
        return True

    def paid_bank(self, num):
        if self.current_player.money >= num:
            self.current_player.money -= num
            return False
        if self.current_player.land_sum >= num:
            while self.current_player.lands:
                sell_Land(self.current_player)
                if self.current_player.money >= tmp_money:
                    self.current_player.money -= num
                    return False
        return True
# def main():
#     #added this line to run the window 
#     my_display = Display()
#     my_display.root.mainloop()
#     # my_display.create_map_frame()

#     player_num = 0
   
#     for i in range(player_num):
#         player_list.append(Player(i+1))
#     while len(player_list) > 1:
#         take_turn(game_map, player_list, player_list[0], 0)
#         player_list.append(player_list[0])
#         player_list.pop(0)
    
  
##Hongyu Xu 
# Roll dice 
def roll_die():
    return random.randint(1, 6)



    

    
        

    
# purchase different types of land


# make the payment 


# make the payment to banke


# load game information from json file
def load_Map():
    lands = []
    with open("Json/monopoly_space_info.json", "r") as file:
        land_dict = json.load(file)
    for i in range(len(land_dict)):
        lands.append(Land(land_dict[i]["Name"], land_dict[i]["Type"], land_dict[i]["HousePrice"], land_dict[i]["Color"], land_dict[i]["Price"], land_dict[i]["Rent"]))
    return lands

    
# sell land 
def sell_Land(player):
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
    with open("Json/take_chance.json") as file_handle:
        chance_card = file_handle.read()
    card_dict = json.loads(chance_card)
    num = random.randint(0,10)
    return card_dict.get(num)

def main():
    #added this line to run the window 
    my_display = Display()
    my_display.root.mainloop()

if __name__ == "__main__":
    main()
