from random import randint

player = raw_input("Rock, Paper, or Scissors? ")
player = str(player)

def comp():
	value = randint(1,3)
	
	if value == 1:
		hand = "rock"
	elif value == 2:
		hand = "paper"
	else:
		hand = "scissors"
		
	return hand
	
def game():

	hand = comp()

	if hand == player:
		print "Tie!"
	elif ((hand == "paper" and player == "rock") or (hand == "scissors") or (hand == 'rock' and player == "scissors")):
		print "You lose!"
	else:
		print "You win!"

game()