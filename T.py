n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
path = [0] * n

def has_cycle(v):
    visited[v] = 1
    path[v] = 1
    for i in range(n):
        if graph[v][i]:
            if not visited[i]:
                if has_cycle(i):
                    return 1
            elif path[i]:
                return 1
    path[v] = 0
    return 0

print(1 if any(has_cycle(i) for i in range(n)) else 0)
