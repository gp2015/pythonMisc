import syracuse_collatz


def test_syracuse():
	case = syracuse_collatz.syracuse(1)
	assert case == 0

	case = syracuse_collatz.syracuse(2)
	assert case == 1 # why doesn't this return 0?

	case = syracuse_collatz.syracuse(3)
	assert case == 0


def test_collatz():
	case = syracuse_collatz.collatz(1)
	assert case == 4

	case = syracuse_collatz.collatz(2)
	assert case == 1