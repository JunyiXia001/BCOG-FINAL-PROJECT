from land import land
from player import player
def main():
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


if __name__ == "__main__":
    main()
