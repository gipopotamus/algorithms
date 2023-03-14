from collections import defaultdict
import sys

sys.setrecursionlimit(20000)
n, m = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
low = [0] * (n+1)
ids = [0] * (n+1)
parent = [-1] * (n+1)
id = 0
cut_points = []


def dfs(node, is_root):
    global id
    visited[node] = True
    low[node] = ids[node] = id
    id += 1
    child_count = 0
    for child in graph[node]:
        if not visited[child]:
            parent[child] = node
            child_count += 1
            dfs(child, False)
            low[node] = min(low[node], low[child])
            if ids[node] <= low[child] and not is_root:
                cut_points.append(node)
        elif child != parent[node]:
            low[node] = min(low[node], ids[child])
    if is_root and child_count > 1:
        cut_points.append(node)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, True)


cut_points = sorted(set(cut_points))
print(len(cut_points))
print(*cut_points, sep='\n')