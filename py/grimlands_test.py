# Scenario
def ne_room():
	prompt()
	if (choice == "use" or choice == "u"):
		use()
		ne_room()
	elif (choice == "inv" or choice == "i" or choice == "inventory"):
		inv()
		ne_room()
	else:
		print "\n\tYou stand there stupidly."
		ne_room()

		
# Use Command		
def use():
	item = raw_input("\n\tWhat item would you like to use?\n\n>").lower()
	if item in inventory:
		print "\n\tYou use the " + item
	else:
		print "\n\tI don't have that, or I can't use that here!"
		

# Prompts for input		
def prompt():
	global choice
	choice = raw_input("\n\tWhat do you do?\n\n>").lower()
	
	
# Inventory
inventory = []
	
def inv():
	print "\n\tYou look in your bag:"
	if len(inventory) == 0:
		print "\n\t[empty]\n"
	else:	
		for item in range(0, len(inventory)):
			itemNum = 1
			print "\n\t" + str(itemNum) + ".) " + inventory[item] + "\n"
			itemNum += 1
		
		
inventory.append('sword')
ne_room()