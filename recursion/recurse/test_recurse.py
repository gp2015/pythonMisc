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