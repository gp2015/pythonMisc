from random import randint
player = input('Rock, Paper, or Scissors?')
player = player.upper()
def comp():
        value = radint(1,3)
        if value == 1:
                hand = 'ROCK'
        elif value == 2:
                hand = 'PAPER'
        elif value == 3:
                hand = 'SCISSORS'
        else:
                print("Oops! We've made a mistake!")
        print (hand)
def game():
        if hand == player:
                print ('We tied!')
        elif (hand == 'PAPER' and player == 'ROCK') or (hand == 'SCISSORS' and player == 'PAPER')\
	or (hand == 'ROCK' and player == 'SCISSORS'):
		print ('You Lose! :(')
	else:
		print('You Win! :)')