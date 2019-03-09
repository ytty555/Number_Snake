n = int(input())

# Забиваем нулями матрицу n x n
matrix = [[0 for x in range(n)] for y in range(n)]

count = 1
i = 0
m = n

while count <= n * n:
    # 1. Идем вправо
    x = i
    y = i
    while x < m:
        matrix[x][y] = count
        x += 1
        count += 1

    # 2. Идем вниз
    x = m - 1
    y = i + 1
    while y < m:
        matrix[x][y] = count
        y += 1
        count += 1

    # 3. Идем влево
    x = m - 2
    y = m - 1
    while x >= i:
        matrix[x][y] = count
        x -= 1
        count += 1

    # 4. Идем вверх
    x = i
    y = m - 2
    while y >= i + 1:
        matrix[x][y] = count
        y -= 1
        count += 1

    i += 1
    m -= 1



# Выводим результирующую матрицу
for y in range(n):
    for x in range(n):
        print(matrix[x][y], end="\t")
    print()
