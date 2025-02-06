def numbers(n):
    triples = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer() and c <= n:
                triples.append((a, b, int(c)))
    return triples

n = int(input("Введіть n: "))
result = numbers(n)

for triple in result:
    print(triple)


