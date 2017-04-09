# SW room
def sw_room():
	print "\n\tYou are in the South West Room." 
	print "\n\tThere are passages leading east and north."
	print "\n\tAs if by magic, when you entered the room, \
\n\ttwo identical guardians of stone moved \
\n\tfrom the corners of the room and now block \
\n\tthe east and north exits."
	prompt()
	if (choice == "look" or choice == "l"):
		print """
	Written on the wall you see a fiery font that reads:
		\n\t\tYou have died and are in limbo. 
		\n\t\tWhat word is magic?"""
		location = sw_room()
	elif (choice == "east" or choice == "e" or choice == "north" or 
	choice == "n"):
		print "\n\tA guardian of stone blocks your path."
		sw_room()
	elif (choice == "inventory" or choice == "i"):
		inv()
		location = sw_room()
	elif (choice == "command" or choice == "commands" or choice == "c" or
	choice == "h" or choice == "help"):
		commands()
		location = sw_room()
	elif (choice == "please" or choice == "pls"):
		print "\n\tYou pass the stone guards freely, but no matter \
\n\twhich door you choose, you awaken here:"
		location = main_room()
	elif (turn == turns):
		main_room()
	else:
		print "\n\t***********************************"
		print "\n\tType 'commands' or 'help' for help."
		print "\n\t***********************************"
		location = sw_room()