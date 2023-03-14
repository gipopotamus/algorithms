def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            dfs(u)
    order.append(v)

def dfs_transpose(v):
    visited[v] = True
    for u in adj_transpose[v]:
        if not visited[u]:
            dfs_transpose(u)

n = int(input())
adj = [[] for _ in range(n)]
adj_transpose = [[] for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            adj[i].append(j)
            adj_transpose[j].append(i)

visited = [False] * n
order = []
for i in range(n):
    if not visited[i]:
        dfs(i)

visited = [False] * n
dfs_transpose(order[-1])
if all(visited):
    print("YES")
else:
    print("NO")
