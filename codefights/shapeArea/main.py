# mine works
def shapeArea(n):
    if n == 0:
        area = 0;
    elif n == 1:
        area = 1
    else:
        area = (n * n) + ((n-1) * (n-1))
    return area


print shapeArea(1)
print shapeArea(2)
print shapeArea(3)
print shapeArea(5)


# working example
def shapeArea(n):
    if n == 1:
        area = 1
    else:
        area = shapeArea(n - 1) + (n - 1) * 4
    return area


print shapeArea(1)
print shapeArea(2)
print shapeArea(3)
print shapeArea(5)
