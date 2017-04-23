import main


def test_shapeArea():
	case = main.shapeArea(1)
	assert case == 1

	case = main.shapeArea(2)
	assert case == 5

	case = main.shapeArea(3)
	assert case == 13

	case = main.shapeArea(5)
	assert case == 41

	case = main.shapeArea(100)
	assert case == 19801