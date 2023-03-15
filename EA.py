# Переписанный код на Python

n, m = map(int, input().split())
g = [[0]*(n+1) for i in range(n+1)]
used = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = g[b][a] = 1

def dfs(v):
    used[v] = 1
    for i in range(1, n+1):
        if g[v][i] == 1 and used[i] == 0:
            print(v, i)
            dfs(i)
    used[v] = 2

dfs(1)
