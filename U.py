def Floyd(n, a):
    # Инициализация матрицы кратчайших путей
    d = [[a[i][j] for j in range(n)] for i in range(n)]

    # Алгоритм Флойда-Уоршелла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    # Поиск минимального пути среди всех найденных
    ans = float('inf')
    for i in range(n):
        for j in range(n):
            if i != j:
                ans = min(ans, d[i][j])

    # Проверка на наличие отрицательного цикла
    for i in range(n):
        if d[i][i] < 0:
            print(-1)
            exit()
    return ans


if __name__ == '__main__':
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    print(Floyd(n, a))