def tvarsumma(n):
    if n == 0:
        return 0
    return (n % 10) + (tvarsumma(n // 10))


print(tvarsumma(abs(335)))
