'''
S(1) = 0
If n is odd, S(n) = 1 + S(3n + 1)
If n is even, S(n) = S(n/2)
'''


def syracuse(num):
	if (num == 0):
		return 0

	if (num == 1):
		return 0

	if (num % 2) == 0:
		return 1 + syracuse((3*num) + 1)
	elif (num % 2) != 0:
		return syracuse(num/2)
	else:
		print("Does not compute!")


print syracuse(1)
print syracuse(2) # positive numbers return 1 instead of 1 returning 0
print syracuse(3)


'''
Take any positive integer n. 
If n is even, divide it by 2 to get n / 2. 
If n is odd, multiply it by 3 and add 1 to obtain 3n + 1.
'''

def collatz(num):
	if (num % 2) == 0:
		return num / 2

	if (num % 2) != 0:
		return 3*num + 1