def buy_a(a, x, y, pieces):
    return (a * pieces, x - pieces)


def buy_c(c, x, y, pieces):
    return (c * pieces, x - pieces, y - pieces)


def calc(a, b, c, x, y):
    if x <= 0 and y <= 0:
        return 0

    total = 0
    if x > 0 and y > 0:
        pieces = min(x, y)
        if a + b > c:
            total = total + c * pieces
        else:
            total = total + ((a + b) * pieces)
        x = x - pieces
        y = y - pieces

    if x > 0:
        if a < c:
            total = total + a * x
        else:
            total = total + c * x
            y = y - pieces
    if y > 0:
        if b < c:
            total = total + b * y
        else:
            total = total + c * y

    return total


a, b, c, x, y = map(int, input().split(" "))
print(calc(a, b, c * 2, x, y))
