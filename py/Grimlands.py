import random

title = """
\n\t\t\t=========
\n\t\t\tGRIMLANDS
\n\t\t\t=========
"""


# The room the player starts in
def main_room():
	print "\n\tYou are in the Main Room."
	print "\n\tYou are in a cold, damp room."
	print "\n\tWhat do you do?"
	prompt()
	if (choice == "look" or choice == "l"):
		print "\n\tThere is a door to the east, a passage leading west, \n\tand a passage \
leading south."
		location = main_room()
		return prompt()
	elif (choice == "east" or choice == "e" or choice == "open" or 
	choice == "o"):
		if ('key' in inventory):
			print "\n\tYou use the key in your inventory to open the locked door."
			return ne_room()
		else:
			print "\n\tThe eastern door is locked and you do not have a 'key'. \
\n\tYou hear heavy breathing on the other side of the door."
			return main_room()
	elif (choice == "west" or choice == "w"):
		print "\n\tYou smell something sickening."
		print "\n\tWith each western step, the smell \
		\n\tbecomes increasingly offensive."
		location = nw_room()
	elif (choice == "south" or choice == "s"):
		print "\n\tYou hear hissing."
		print "\n\tWith each southern step, the hissing \
\n\tincreases in amplitude."
		location = south_room()
	elif (choice == "inventory" or choice == "i"):
		inv()
		main_room()
	elif (choice == "command" or choice == "commands" or choice == "c" or
	choice == "h" or choice == "help"):
		commands()
		location = main_room()	
	else:
		print "\n\t***********************************"
		print "\n\tType 'commands' or 'help' for help."
		print "\n\t***********************************"
		location = main_room()

	
# NW room with troll
def nw_room():
	print "\n\tYou are in the North West Room."
	print "\n\tThere is a passage leading east."
	
	troll = True
	
	while troll:
		print "\n\tYou are face to face with a large, smelly troll \
	\n\tguarding a golden treasure chest. \
	\n\tThe troll appears to be asleep."
		prompt()
		if (choice == "look" or choice == "l"):
			location = nw_room()
			return prompt()
		elif (choice == "east" or choice == "e"):
			location = main_room()
		elif (choice == "open" or choice == "o"):
			print "\n\tThe smelly, sleeping troll blocks your way to the chest."
			print "\n\tIf only there was a way to get rid of this smelly troll..."
		elif (choice == "inventory" or choice == "i"):
			inv()
			location = nw_room()
		elif (choice == "command" or choice == "commands" or choice == "c" or
	choice == "h" or choice == "help"):
			commands()
			location = nw_room()
		elif (choice == "sneak"):
			sneakDC = 12
			sneaking = sneak()
			if ('key' not in inventory and sneaking >= sneakDC):
				print "\n\tYou sneak up to the sleeping troll and pickpocket \
\n\ta small 'key'!"
				inventory.append('key')
				print "\n\tA small 'key' has been added to your inventory! \
\n\tMaybe this 'key' is for a door somewhere?"
			elif (sneaking == 1):
				print "\n\tYour clumsiness wakes the troll from its slumber."
				print "\n\tThe troll screams ferociously in your face. The \
\n\tsmell is nauseating. You faint."
				main_room()
			elif (sneaking != 1 and sneaking < sneakDC and 'key' not in inventory):
				print "\n\tThe troll grunts, but is not awoken. You inch closer."
				nw_room()
			elif ('key' in inventory):
				print "\n\tThe troll doesn't have anything else!"

		else:
			print "\n\t***********************************"
			print "\n\tType 'commands' or 'help' for help."
			print "\n\t***********************************"
			location = nw_room()

			
# NW room without troll			
		
		
# NE room
def ne_room():
	print "\n\tYou are in the North East Room."
	print "\n\tYou are face to face with an enormous Owlbear guarding a \
\n\tgolden treasure chest adorned with jewels."
	prompt()
	if (choice == "look" or choice == "l"):
		print "\n\tThere is an unlocked door to the west."
		location = ne_room()
		return prompt()
	elif (choice == "west" or choice == "w"):
		print "\n\tAs if by magic, the North East Room door locks behind you."
		location = main_room()
	elif (choice == "inventory" or choice == "i"):
		inv()
		location = ne_room()
	elif (choice == "command" or choice == "commands" or choice == "c" or
	choice == "h" or choice == "help"):
		commands()
		location = ne_room()
	elif (choice == "open" or choice == "o"):
		print "\n\tThe enormous Owlbear blocks your way to the chest."
		print "\n\tIf only there was a way to get rid of the enormous Owlbear..."
		location = ne_room()
	elif (choice == "sneak"):
		sneakDC = 15
		sneaking = sneak()
		print sneaking
		print choice
		if ('sword' not in inventory and sneaking >= sneakDC):
			print "\n\tThe Owlbear lost sight of you, and begins to walk around the room. \
			\n\tThe golden chest adorned with jewels is no longer blocked by the \
			\n\tOwlbear!"
			print "\n\tThe chest is locked. You use the 'key' that unlocked the door \
			\n\tto this room, and it becomes stuck in the chest's keyhole."
			inventory.remove('key')
			print "\n\tYou open the golden chest adorned with jewels."
			print "\n\tYou receive a large 'sword'!"
			inventory.append('sword')
			print "\n\tThe Owlbear notices you and is enraged."
			location = main_room()
					
		elif (sneaking == 1):
			print "\n\tAs you try to sneak to the chest, the Owlbear turns to face you. \
			\n\tThe Owlbear tears you to shreds."
			location = main_room()
			
		elif (sneaking != 1 and sneaking < sneakDC and 'sword' not in inventory):
			print "\n\tThe Owlbear is watching you."
			location = ne_room()
			
	else:
		print "\n\t***********************************"
		print "\n\tType 'commands' or 'help' for help."
		print "\n\t***********************************"
		location = ne_room()


# South room with Snakes
def south_room():
	print "\n\tYou are in the South Room."
	print "\n\tThis room is darker still. \n\
\n\tThere is a passage leading north, \
\n\tand a door to the east."
	
	snakes = True
		
	if snakes:
		print "\n\tYou sense motion in the dark."
		prompt()
		if (choice == "look" or choice == "l"):
			print "\n\tThe floor writhes."
			print "\n\tTreasures of gold and jewels litter the room. \
	\n\tCountless snakes slither and crawl over everything \
	\n\tin this room, including a golden treasure chest."
			location = south_room()
			return prompt()
		elif (choice == "north" or choice == "n"):
			print "\n\tWith each northern step, the sound of hissing fades \
	\n\tfurther into the abyss that lies behind you."
			location = main_room()
		elif (choice == "east" or choice == "e"):
			print "\n\tSlithering snakes cover everything in this room, \
			\n\tincluding the eastern door."
			print "\n\tIf only there was a way to get rid of these snakes..."
			return south_room()
		elif (choice == "open" or choice == "o"):
			print "\n\tSlithering snakes cover everything in this room, \
			\n\tincluding the golden treasure chest."
			print "\n\tIf only there was a way to get rid of these snakes..."
			return south_room()
		elif (choice == "inventory" or choice == "i"):
			inv()
			location = south_room()
		elif (choice == "use" or choice == "u"):
			item = use()
			if (item == 'sword'):
				sword_for_snakes()
			elif (item == 'snake charm'):
				snake_charm()
			else:
				south_room()
		else:
			print "\n\t***********************************"
			print "\n\tType 'commands' or 'help' for help."
			print "\n\t***********************************"
			location = south_room()
		
	else:
		south_room_no_snakes()


# South room without snakes
def south_room_no_snakes():
	print "\n\tThis room is darker still. \n\
\n\tThere are passages leading north and west. \
\n\tThere is a door to the east."
	print "\n\tThe room is quiet and there is a golden treasure chest."
	prompt()
	if (choice == "look" or choice == "l"):
		location = south_room_no_snakes()
		return prompt()
	elif (choice == "open" or choice == "o"):
		open()
	elif (choice == "north" or choice == "n"):
		print "\n\tWith each northern step, the sound of hissing fades \
\n\tfurther into the abyss that lies behind you."
		location = main_room()
	else:
		print "\n\tType 'commands' or 'help' for help.\n"
		location = south_room_no_snakes()


# Boss room
	
# Inventory: lists items in numbered order

inventory = []

def inv():
	print "\n\tYou look in your bag: \n"
	if len(inventory) == 0:
		print "\n\t[empty]\n"
	else:
		itemNum = 1
		for item in range(0, len(inventory)):
			print "\t" + str(itemNum) + ") " + inventory[item]
			itemNum += 1
		print "\n"
	

# Snake Charm
	# Prompts user to use snake charm if they have it when entering South Room
def snake_charm():
	if ('snake charm' in inventory):
		choice = raw_input("\n\tWould you like to charm the snakes in this room?\
		\n\nType 'yes' or 'no': ").lower()
		if (choice == "yes" or choice == "y"):
			print "\n\tThe snakes are charmed. They disperse into the walls."
			snakes = False
			south_room_no_snakes()
		else:
			print "\n\tYou do not charm any snakes."
			snakes = True
			south_room()
	else:
		snakes = True
	

# Sword for Snakes
def sword_for_snakes():	
	if ('sword' in inventory):
		choice = raw_input("\n\tWould you like to attack the snakes in this \
room with your sword?\n\nType 'yes' or 'no': ").lower()
		if (choice == "yes" or choice == "y"):
			print "\n\tYou cut the heads off of a few snakes. The rest disperse into \
the walls."
			snakes = False
			south_room_no_snakes()
		else:
			print "\n\tYou do not kill any snakes."
			snakes = True
			south_room()
	else:
		if snakes == True:
			snakes = True
		else:
			snakes = False
	
		
# Commands
def open():
	what_to_open = raw_input("\n\tWhat do you want to open? \n\n> ").lower()
	if (what_to_open == "chest" or "c"):
		if ('key' in inventory):
			print "\n\tThe chest opens."
		else:
			print "\n\tYou need a key to open this chest."
	elif (what_to_open == "door" or "d"):
		if ('key' in inventory):
			print "\n\tThe door opens."
		else:
			print "\n\tYou need a key to open this door."


# Use command		
def use():
	what_to_use = raw_input("\n\tWhat item would you like to use? \n\n> ").lower()
	if (what_to_use == 'snake charm' and 'snake charm' in inventory):
		print "\n\tYou use the snake charm!"
		return 'snake charm'
	elif (what_to_use == 'sword' and 'sword' in inventory):
		print "\n\tYou use the sword!"
		return 'sword'
	else:
		print "\n\tI don't seem to have that, or I can't use that here."
			
# Help menu
def commands():
	commands = ['look, l', 'north, n', 'east, e', 'south, s', 'west, w', \
	'open, o', 'inventory, i', 'use, u', 'sneak']
	
	print "\n\t*************************************************"
	print "\n\tType 'commands' or 'help' to see this menu again."
	print "\n\t*************************************************"
	print "\n\tType any of the following commands: \n"
	for command in commands:
		print "\t\t" + command + "\n"
	print "\t*************************************************"	


def sneak():
	roll = random.randint(1,20)
	return roll
	
# Prompts user for input	
def prompt():
	global choice
	choice = raw_input("\n> ").lower()


	
# Game begins
commands()
print title
location = main_room()
