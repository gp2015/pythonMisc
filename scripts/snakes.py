# Prompts user to use snake charm if they have it when entering South Room
	if ('snake charm' in inventory and snakes == True):
		choice = raw_input("\n\tWould you like to charm the snakes in this room?\
		\n\nType 'yes' or 'no': ").lower()
		if (choice == "yes" or choice == "y"):
			print "\n\tThe snakes are charmed. They disperse into the walls."
			snakes = False
			south_room_no_snakes()
		elif (choice == "no" or choice == "n"):
			print "\n\tYou do not charm any snakes."
			snakes = True
			choice = ""
		else:
			# print "\n\tWould you like to use the snake charm?"
			location = south_room()
	else:
		snakes = True
		
	# Prompts user to use sword if they have it when entering South Room	
	if ('sword' in inventory and snakes == True):
		choice = raw_input("\n\tWould you like to attack the snakes in this \
room with your sword?\n\nType 'yes' or 'no': ").lower()
		if (choice == "yes" or choice == "y"):
			print "\n\tYou cut the heads off of a few snakes. The rest disperse into \
the walls."
			snakes = False
			south_room_no_snakes()
		elif (choice == "no" or choice == "n"):
			print "\n\tYou do not kill any snakes."
			snakes = True
			choice = ""
		else:
			# print "\n\tWould you like to use the sword?"
			location = south_room()
	else:
		if snakes == True:
			snakes = True
		else:
			snakes = False