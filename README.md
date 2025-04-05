# BCOG-FINAL-PROJECT
Topic: Monopoly\
Our program is a simple simulator of the board game "Monopoly." Monopoly is an economic-themed broad game, and players will roll dice to make decisions and move on the board, such as purchasing land, paying rent, or having special events. Finally, the player with the most money will win the game and lose when the player goes bankrupt. 

Function A:\
This is the main function that allows players to choose the action term by term. 

Function B:\
We will have a class map that includes the land price/ rent and special events. 

Function C:\
We have a class of players that shows up the money and the ownership of the land.    


Group members:\
Name    | Username \
Junyi Xia  JunyiXia001\
Hongyu Xu  RaidriarXu

Work\
One person will devolop the class/function of players.(Function C)\
One person will develop the map (Function B)\
At last, we will develop the main functuion of the game together. (Function A)


Communication\
Members in our group communicate through webchat and zoom. We will have 2 meetings per week to discuss the program and related issues. Also, we can text each other if anyone have other/emergency issues. 



**Documentatation**\
The logic of our program is sperated into two major parts which are game logic and it's visualization. Our program mimics the Monopoly broad game through Tkinter and load map data through JSON file.Our program have four major components：

Display class visualizes the game.\
Take_turn method provides the main logic of the game (movememt, place tracking, space info)\
Load Map function provide the information of each space in the game.\
Buyland, sell land functions allow players to manage their assets.\
Take chance function generates random events from a set of predefined Chance cards.\

**Function description**\
Display class\
-visualization of the game (Map, information panel, buttons)\
**Function**\
create_map_frame(), create_interface_frame(), create_information_panel(): game UI components.\
next_turn():advances to the next player's turn.\
take_turn(game_map, player_list, player, count): player's turn, roll dice, movement, rent check, jail status check, land purchase.\
message():print message in the information panel; takes string as an input.\
roll_die(): return a random int between 1 and 6.\
buyLand(player, land): pruchase land and player money deduction.\
paid(player, receiver, num): return boolean variable, and transefer money between players(rent).
sellLand(player): allowing players to sell their assets.\
laodMap(): Load information of each space in the map, return the value as list.\
take_chance(): choose events randomly and return it as a string.

**Example Uses Case**
This game designed for people that interested in playing broad game, which allows players to play on computer if they don't have physical cards or board. 

**Input File**
monopoly_space_info.json: JSON file\
take_chance.json: JSON file\
land.py: python file\
player.py: python file\


**Test Case**


