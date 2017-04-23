def shapeArea(n):
    if n == 1:
        area = 1
    else:
        area = (n * n) + ((n-1) * (n-1))
    return area


def shapeArea(n):
    if n == 1:
        area = 1
    else:
        area = shapeArea(n - 1) + (n - 1) * 4
    return area