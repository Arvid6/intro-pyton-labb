def derivative(f, x, h):
    return 1/(2*h)*(f(x+h)-f(x-h))


def function(x):
    return 2**x - 4


def solve(f, x0, h):
    x = h
    while True:
        if abs(x0 - x) < h:
            return x0
        x = x0
        x0 = x0 - f(x0)/derivative(f, x0, h)


der = solve(function, 10, 0.000000001)
print(der)
