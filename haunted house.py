"""from datetime import datetime

now = datetime.now()

print "%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second)"""



def haunted_house():
    print "Welcome to the house where you will DIE!"
    print "What direction would you like to go?"
    answer = raw_input("Type a direction and hit 'Enter'.").lower()
    if answer == "forward" or answer == "f":
        print "You fall through a trap door and DIE."
        haunted_house()
    elif answer == "backward" or answer == "b":
        print "An axe falls from the ceiling and slices you in half. You DIE."
        haunted_house()
    elif answer == "left" or answer == "l":
        print "A vampire stands in front of you. Trust me, you DIE."
        haunted_house()
    elif answer == "right" or answer == "r":
        print "Your mother in law stands before you. YOU WISH YOU COULD JUST DIE."
        haunted_house()
    elif answer == "up" or answer == "u":
        print "You jump too high and break your ankle when you land. You will eventually DIE."
        haunted_house()
    elif answer == "down" or answer == "d":
        print "To the pits of hell you fall. Here you will experience eternal torment, pain and unrest, but will never DIE."
        haunted_house()
    else:
        print "You failed to enter a direction. Hands come out of the floor and pull your under the house. You DIE."
        haunted_house()

haunted_house()

