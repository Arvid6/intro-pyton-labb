#
def kostnad(p, r, a):
    k = int(p + (a + 1) * ((p * r) / 2))
    print("Den totala kostnaden efter", a, "år är", k, "kr")


kostnad(50000, 0.03, 10)

