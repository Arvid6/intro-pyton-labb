def tvarsumma2(n):
    value = 0
    for x in range(n):
        if n == 0:
            return value
        value += n % 10
        n //= 10


print(tvarsumma2(abs(1234)))
