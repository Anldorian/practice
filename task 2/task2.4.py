def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

n = int(input("Введіть число: "))
factors = prime_factorization(n)

print(f"{n} =", ", ".join(map(str, factors)))