import recurse


def test_syracuse():
	case = recurse.syracuse(1)
	assert case == 0

	case = recurse.syracuse(2)
	assert case == 0

	case = recurse.syracuse(3)
	assert case == 0


def test_collatz():
	case = recurse.collatz(1)
	assert case == 1

	case = recurse.collatz(2)
	assert case == 1

	case = recurse.collatz(3)
	assert case == 1


def test_fib():
	case = recurse.get_fib(0)
	assert case == None

	case = recurse.get_fib(1)
	assert case == [1]

	case = recurse.get_fib(2)
	assert case == [0, 1, 1]

	case = recurse.get_fib(3)
	assert case == [0, 1, 1]

	case = recurse.get_fib(5)
	assert case == [0, 1, 1, 2, 3]

	case = recurse.get_fib(6)
	assert case == [0, 1, 1, 2, 3, 5]

	case = recurse.get_fib(10)
	assert case == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

	case = recurse.get_fib(20)
	assert case == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]