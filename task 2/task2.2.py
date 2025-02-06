def pascal(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

n = int(input("Введіть кількість рядків: "))
triangle = pascal(n)

for row in triangle:
    print(" ".join(map(str, row)))
