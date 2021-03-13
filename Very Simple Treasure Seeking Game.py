#!/usr/bin/env python3
import time
import random
try:
    excepted=False
    from prettytable import PrettyTable
except ModuleNotFoundError:
    excepted=True
except ImportError:
    excepted=True
if excepted:
    print("Required Module - prettytable not satisfied.\nInstall with 'python -m pip install prettytable'")
    input("Press Any Key To Exit.")
    exit()

# Assigning Size, Treasure Coordinate, and Player Coordinate
# size (y, x) 
# reversed because 2d list is so
size = [15, 15]
treasure = [random.randint(0, size[0]-1), random.randint(0, size[1]-1)]
player = [0,0]


def map_maker(size, player, treasure):
    map = []
    for x in range(size[0]):
        curr_line = []
        for y in range(size[1]):
            if [x, y] == player:
                curr_line.append("P")
            elif [x, y] == treasure:
                curr_line.append("X")
            else:
                curr_line.append("-")
        map.append(curr_line)
    return map


def help():
    help_list = ['HELP','', 'P is You', 'X is The Treasure', '', 'Controls','Move with W A S D.', 'W - Go Up', 'A - Go Left', 'S - Go Down', 'D - Go Right', 'Have Fun!']
    help_list = [f"│{f'{line}':<{len(max(help_list, key=len))}}│" for line in help_list]
    print(f"┏{'':━<18}┓")
    for line in help_list:print(line)
    print(f"┗{'':━<18}┛\n")


print("Welcome To The Treasure Seeking Game!\nIn this game your goal is to go to the X marked location. Good Luck Adventurer!\n\n")
#help() # Show Help


while True:
    # Getting the current map and print it with PrettyTable
    table = map_maker(size, player, treasure)
    pt = PrettyTable()
    for row in table:pt.add_row(row)
    print(pt.get_string(header=False))
    
    #Check if player get the treasure, if true, congratulate player and exits
    if player == treasure:
        print("Congratulations on winning the game!")
        countdown = 3
        for i in range(countdown, 0, -1):
            print(f"{f'Exiting in {i} Seconds':<30}", end="\r")
            time.sleep(1)
        print(f"{f'Exiting...':<30}")
        exit()
    
    # Asking player input and work with it.
    direction = input("\nDirection(type help for help):").upper()
    if direction == "D" and player[1] != size[1]:
        player[1]+=1
    elif direction == "S" and player[0] != size[0]:
        player[0]+=1
    elif direction == "A" and player[1] != 0:
        player[1]-=1
    elif direction == "W" and player[0] != 0:
        player[0]-=1
    elif direction in ['HELP', 'H', 'DIRECTION', 'DIRECTIONS', 'DIR']:
        help()
    else:
        print("Invalid Action.\n\n\n")
    
