'''
S(1) = 0
If n is odd, S(n) = 1 + S(3n + 1)
If n is even, S(n) = S(n/2)
'''


def syracuse(num):
	if (num == 0) or (num == 1):
		return 0

	if (num % 2) == 0:
		return syracuse(1 + syracuse((3*num) + 1))
	elif (num % 2) != 0:
		return syracuse(num/2)


'''
Take any positive integer n. 
If n is even, divide it by 2 to get n / 2. 
If n is odd, multiply it by 3 and add 1 to obtain 3n + 1.
'''

def collatz(num):
	if (num == 0) or (num == 1):
		return 1

	if (num % 2) == 0:
		return collatz(num / 2)

	if (num % 2) != 0:
		return collatz(3*num + 1)


# init fib array
# no indices exist yet, so cannot fib[0] = num
# have to .append to allocate memory
fib = []
fib.append(1)
fib.append(1)
fib.append(2)


# get first num numbers in fib
def get_fib(num):
	# base cases 0, 1
	if num == 0:
		exit
		
	if num == 1:
		
	else:
		# start at 1 because fib[0] and fib[1] already allocated
		for i in range(2, num):
			next = fib[i - 1] + fib[i - 2]
			fib.append(next)
	return fib
		

print get_fib(0)
print get_fib(1)
print get_fib(2)
print get_fib(3)
print get_fib(5)
print get_fib(6)
print get_fib(10)
print get_fib(20)