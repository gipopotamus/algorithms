n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

# Построение транзитивного замыкания
for k in range(n):
    for i in range(n):
        for j in range(n):
            adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])

# Вывод матрицы транзитивного замыкания
for i in range(n):
    print(*adj_matrix[i])
