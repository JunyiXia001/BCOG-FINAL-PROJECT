from src.land import Land
from src.player import Player
import random
import tkinter as tk
from PIL import Image, ImageTk
import json
from tkinter import ttk
from tkinter import messagebox
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
player_color = {
    1:"green", 2:"red", 3:"yellow", 4:"blue"
}
### MainFrame and Map display 
class Display:   
    screen_size = (1280, 720)
    def __init__(self):
        #Basic setup of display function 
        self.root = tk.Tk()
        self.player_num = 2
        self.init_window()
        self.game_map = load_Map()
        self.player_list = {i + 1 : Player(i + 1) for i in range(self.player_num)} 
        self.player_icon = []
        for player in self.player_list.values():
            x, y = self.game_map[0].location
            size = 20
            rec = self.map_canvas.create_rectangle(
            x , y , x + size , y + size,
            fill=player_color[player.id],
            outline='black',
            width=2, tag = player.id)
            self.player_icon.append(rec)
    
        self.current_player = self.player_list[1]
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
        self.upgrade_button = tk.Button(self.interface_frame, text = "build house", command=self.call_upgrade, bg = "yellow")
        self.upgrade_button.pack(side = "left",padx=10, pady=10)
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
        self.map_canvas.create_image(self.map_width // 2,self.map_height // 2, image=self.map_img, anchor=tk.CENTER, tags="map_image")
        
  


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
        self.message("Click Go! to start the game! Good Luck!\n\n")
    # connect button with take turn method 

    def call_take_turn(self):
        self.message(f"It's {self.current_player.name}'s turn.")
        self.message(f"money: {self.current_player.money}\n")
        self.take_turn()
        # self.buy_button.pack_forget()
        self.take_turn_button.pack_forget()
        self.End_button.pack(side = "right",padx=10,pady=10)
    # connect button with buy land method 

    def call_buy_land(self):
        self.buy_Land()
        self.message(f"this land is now {self.game_map[self.current_player.position].owner}\n\n")
        self.buy_button.pack_forget()
    # function in side of class which call the sell land function
    def call_sell_land(self):
        sell_interface = tk.Toplevel()
        sell_interface.title("Choose an Image")
        sell_interface.geometry("800x600")
        top_frame = tk.Frame(sell_interface)
        top_frame.pack(pady=10)
        
        canvas_frame = tk.Frame(sell_interface)
        canvas_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(canvas_frame)
        scrollbar = tk.Scrollbar(canvas_frame, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=scrollbar.set)

        scrollbar.pack(side="bottom", fill="x")
        canvas.pack(side="left", fill="both", expand=True)

        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        #Message box setting 
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        scrollable_frame.bind("<Configure>", on_configure)
        #Inner window set up 
        def sell_update_canvas():
            for i in top_frame.winfo_children():
                i.destroy()
            for i in scrollable_frame.winfo_children():
                i.destroy()
            self.money_label = tk.Label(top_frame, text=f"Your Money: ${self.current_player.money}")
            self.money_label.pack()  
            images_info = []
            for land in self.current_player.lands:
                if land.level >= 2:
                    images_info.append({"path": "image/house.png", "description": f"Name: {land.name}\nLevel: {land.level}\n\nYou are selling house, price is {land.house_price/2}"})
                else:
                    images_info.append({"path": "image/house.png", "description": f"Name: {land.name}\nLevel: {land.level}\n\nYou are selling lands, price is {int(land.price*0.7)}"})

            self.photo_images = [] 
            for i, info in enumerate(images_info):
                img = Image.open(info['path'])
                img = img.resize((200, 200)) 
                photo = ImageTk.PhotoImage(img)
                self.photo_images.append(photo)  

                img_label = tk.Label(scrollable_frame, image=photo)
                img_label.grid(row=0, column=i, padx=10)

                desc_label = tk.Label(scrollable_frame, text=info['description'], wraplength=180)
                desc_label.grid(row=2, column=i)

                select_button = tk.Button(scrollable_frame, text="Select", command=lambda x=i: sell_selected(x))
                select_button.grid(row=3, column=i, pady=10)
        #function of selling house 
        def sell_selected(i):
            curr_land = self.current_player.lands[i]
            if curr_land.level > 1:
                curr_land.level -= 1
                self.current_player.money += curr_land.house_price/2
            else:
                curr_land.owner = 0
                self.current_player.money += int(curr_land.price*0.7)
                self.current_player.lands.remove(curr_land)
                for land in self.current_player.lands:
                    if land.color == curr_land.color and land.level == 1:
                        land.level = 0
            sell_update_canvas()
        sell_update_canvas()
            
        sell_interface.mainloop()
    # function of upgrading house 
    def call_upgrade(self):
        upgrade_interface = tk.Toplevel()
        upgrade_interface.title("Choose an Image")
        upgrade_interface.geometry("800x600")
        

        def upgrade_selected(i):
            curr_land = upgradable[i]
            if self.current_player.money < curr_land.house_price:
                self.message("not enough money to build a house")
            else:
                curr_land.level += 1
                self.current_player.money -= curr_land.house_price
                if curr_land.level < 1 or land.level > 6:
                    upgradable.remove(curr_land)
            self.money_label.config(text=f"Your Money: ${self.current_player.money}")
            upgrade_interface.destroy()

        upgradable = []
        for land in self.current_player.lands:
            if land.land_type == "Property" and land.level >=1 and land.level <= 5:
                add = True
                for land2 in self.current_player.lands:
                    if land2.color == land.color and land2.level < land.level:
                        add = False
                        break
                if add:
                    upgradable.append(land)
                        
        images_info = []
        for land in upgradable:
            images_info.append({"path": "image/house.png", "description": f"Name: {land.name}\ncurrent Level: {land.level}\nbuild a house cause{land.house_price}"})
        
        top_frame = tk.Frame(upgrade_interface)
        top_frame.pack(pady=10)

        self.money_label = tk.Label(top_frame, text=f"Your Money: ${self.current_player.money}")
        self.money_label.pack()
        
        canvas_frame = tk.Frame(upgrade_interface)
        canvas_frame.pack(fill="both", expand=True)
        canvas = tk.Canvas(canvas_frame)
        scrollbar = tk.Scrollbar(canvas_frame, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=scrollbar.set)

        scrollbar.pack(side="bottom", fill="x")
        canvas.pack(side="left", fill="both", expand=True)

        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        scrollable_frame.bind("<Configure>", on_configure)

        self.photo_images = [] 
        for i, info in enumerate(images_info):
            img = Image.open(info['path'])
            img = img.resize((200, 200)) 
            photo = ImageTk.PhotoImage(img)
            self.photo_images.append(photo)  
            img_label = tk.Label(scrollable_frame, image=photo)
            img_label.grid(row=0, column=i, padx=10)
            desc_label = tk.Label(scrollable_frame, text=info['description'], wraplength=180)
            desc_label.grid(row=2, column=i)
            select_button = tk.Button(scrollable_frame, text="Select", command=lambda x=i: upgrade_selected(x))
            select_button.grid(row=3, column=i, pady=10)
        
        upgrade_interface.mainloop()

    #End Game detection 
    def call_end(self):
        self.End_button.pack_forget()
        if len(self.player_list) == 1:
            winner = next(iter(self.player_list.values()))
            winner_popup = tk.Toplevel()
            winner_popup.title("Game Over")
            winner_popup.geometry("300x150")
            tk.Label(winner_popup, text=f"{winner.name} is the winner!", font=("Helvetica", 14, "bold")).pack(pady=30)
            tk.Button(winner_popup, text="OK", command=winner_popup.destroy).pack(pady=10)

        else:
            index = (self.current_player.id) % len(self.player_list)
            while index + 1 not in self.player_list:
                index = (index + 1) % len(self.player_list)
            self.current_player = self.player_list[index + 1]
            self.take_turn_button.pack(side = "right",padx=10, pady=10)



    # setup for message box 
    # Source from stackoverflow Date: 4/3/2025 Link: https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only?
    def message(self, message):
        self.info_frame.config(state="normal")
        self.info_frame.insert("end", message + "\n")
        self.info_frame.see("end")
        self.info_frame.config(state="disabled")

    # take turn for player 
    def take_turn(self):

        # Check player's jail status
        
        if self.current_player.jail_status > 0:
            self.current_player.jail_status -= 1
            jail_popup = tk.Toplevel()
            jail_popup.title("You're in Jail")
            jail_popup.geometry("300x150")
            self.current_player.jail_status -= 1

            def pay():
                self.current_player.jail_status = 0
                self.current_player.money -= 50
                messagebox.showinfo("Info", "You paid $50 to get out of jail.")
                jail_popup.destroy()

            def roll():
                die1 = roll_die()
                die2 = roll_die()
                if die1 != die2:
                    messagebox.showinfo("Roll Result", f"You rolled {die1} and {die2} (not a double). You stay in jail.")
                    jail_popup.destroy()
                    self.call_end()
                    return
                else:
                    self.current_player.jail_status = 0
                    messagebox.showinfo("Roll Result", f"You rolled a double: {die1} and {die2}. You're free!")
                    jail_popup.destroy()
                    return
            tk.Label(jail_popup, text="Choose your action:").pack(pady=10)
            tk.Button(jail_popup, text="Pay $50", command=pay).pack(pady=5)
            tk.Button(jail_popup, text="Roll for double", command=roll).pack(pady=5)
            return
        
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
        self.current_player.position = (self.current_player.position + 1) % 40
        land = self.game_map[self.current_player.position]
        self.message(f"{self.current_player.name} go to {land.name}.\n")
        self.move_player_icon(land.location, self.current_player.id)
        
        # self.current_player.position = (self.current_player.position + die1 + die2) % 40

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
                    num = self.game_map[self.current_player.position].rent_Num()

                    self.paid(self.current_player.id, self.game_map[self.current_player.position].owner, num)
        #Railroad
        elif self.game_map[self.current_player.position].land_type == "Railroad":
            if self.game_map[self.current_player.position].pledge == False:
                if self.game_map[self.current_player.position].owner == 0:
                    self.message("do you want to buy the land?\n")
                    self.buy_button.pack(side = "right",padx=10, pady=10)
                elif self.game_map[self.current_player.position].owner != 0 and self.game_map[self.current_player.position].owner != self.current_player.id:
                    num = self.game_map[self.current_player.position].rent_Num()
                    self.paid(self.current_player.id, self.game_map[self.current_player.position].owner, num)
        #Utility 
        elif self.game_map[self.current_player.position].land_type == "Utility":
            if self.game_map[self.current_player.position].pledge == False:
                if self.game_map[self.current_player.position].owner == 0:
                    self.message("do you want to buy the land?\n")
                    self.buy_button.pack(side = "right",padx=10, pady=10)
                elif self.game_map[self.current_player.position].owner != 0 and self.game_map[self.current_player.position].owner != self.current_player.id:
                    num = self.game_map[self.current_player.position].rent_Num(die1 + die2)
                    self.paid(self.current_player.id, self.game_map[self.current_player.position].owner, num)
        #Jail
        elif self.game_map[self.current_player.position].land_type == "Jail":
            self.current_player.position = 10
            self.move_player_icon(self.game_map[10].location, self.current_player.id)
            self.current_player.jail_status = 2
        #Income tax
        elif self.game_map[self.current_player.position].land_type == "Income Tax":
            self.paid_bank(200)
        #Luxury Tax
        elif self.game_map[self.current_player.position].land_type == "Luxury Tax":
            self.paid_bank(100)
        #Take chance
        elif self.game_map[self.current_player.position].land_type == "Chance":
            self.message("player takes a chance")
            chance = take_chance() 
            if chance["Card"] == "Money":
                self.current_player.money += chance["Effect"]
                self.message(f"Player recieve {chance["Effect"]} $")
            elif chance["Card"] == "Tax":
                self.current_player.money += chance["Effect"]
                self.message(f"Player recieve {chance["Effect"]} $")
                


        #use previous one_more and count to decide whether the player have another moving chance
        

    #buy land
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
                            if i.level == 0:
                                i.level += 1
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
        else:
            self.message("you don't have enough money")
    #M Make payment (paying rent)
    def paid(self, player, receiver, num):
        self.message(f"{self.player_list[player].name} pay {self.player_list[receiver].name} money by {num}")
        if self.player_list[player].money >= num:
            self.player_list[player].money -= num
            self.player_list[receiver].money += num
        elif self.player_list[player].land_sum() >= num:
            self.message(f"you have to sell properties to pay")
            while self.player_list[player].lands:
                self.call_sell_land()
                if self.player_list[player].money >= num:
                    self.player_list[player].money -= num
                    self.player_list[receiver].money += num
                    break
        elif self.player_list[player].land_sum() < num:
            self.message(f"{self.player_list[player].name} is out")
            self.player_list[receiver].money += self.player_list[player].land_sum()
            for land in self.player_list[player].lands:
                land.owner = 0
                land.level = 0
            del self.player_list[player]

    def paid_bank(self, num):
        self.message(f"{self.current_player.name} pay bank money by {num}")
        if self.current_player.money >= num:
            self.current_player.money -= num
        elif self.current_player.land_sum() >= num:
            self.message(f"you have to sell properties to pay")
            while self.current_player.lands:
                self.call_sell_land()
                if self.current_player.money >= num:
                    self.current_player.money -= num
                    break
        elif self.current_player.land_sum() < num:
            self.message(f"{self.current_player.name} is out")
            for land in self.current_player.lands:
                land.owner = 0
                land.level = 0
            del self.player_list[self.current_player.id]
    

    # Player visualization 
    def move_player_icon(self, location_input, id):
        
        if location_input is None:
            ("Location not found")
            return
            
        
        x, y = location_input
        size = 20
        self.map_canvas.move(self.player_icon[id - 1], x - self.map_canvas.coords(self.player_icon[id - 1])[0], y - self.map_canvas.coords(self.player_icon[id - 1])[1])
    
# Roll dice 
def roll_die():
    return random.randint(1, 6)



    



# load game information from json file
def load_Map():
    lands = []
    with open("Json/space_location.json", "r") as file:
        loc_info = json.load(file)
    with open("Json/monopoly_space_info.json", "r") as file:
        land_dict = json.load(file)
    for i in range(len(land_dict)):
        loc = loc_info[str(i)]
        lands.append(Land(land_dict[i]["Name"], land_dict[i]["Type"], land_dict[i]["HousePrice"], land_dict[i]["Color"], land_dict[i]["Price"], land_dict[i]["Rent"], location=loc))
  
        

    return lands

#load coordinate forthe location
def load_location():
    location = []
    with open("Json/space_location.json", "r") as file:
        loc_info = json.load(file)
    for i in range(len(loc_info)):
        location.append(loc_info[str(i)])
    return location


## chance situation
def take_chance():
    with open("Json//chance_card.json") as file_handle:
        chance_card = json.load(file_handle)
    num = random.randint(0, len(chance_card) - 1)
    return chance_card[num]

def main():
    #added this line to run the window 
    my_display = Display()
    my_display.root.mainloop()

if __name__ == "__main__":
    main()
