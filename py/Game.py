__author__ = 'George'
inventory = []

inventory.append("pizza oven")
inventory.append("ball of string")

inventory.index("ball of string")
#if/else player has item or not

def main_room():
    print "You are in a cold, damp room. There are 2 doors and 1 chest. What will you do?"
    print "You can do the following things:\n"
    "* 'L' - Explore the door to your left.\n"
    "* 'R' - Explore the door to your right.\n"
    "* 'O' - Open the chest in front of you.\n"
    "* 'I' - Examine your inventory.\n"
    "* 'A' - Look around.\n"

main_room()

#Take player's choice
choice = input("What do you do?: ")