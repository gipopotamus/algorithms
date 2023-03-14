import math

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# Floyd-Warshall algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# Find the maximum distance between any two vertices
max_distance = -math.inf
for i in range(n):
    for j in range(n):
        if i != j:
            max_distance = max(max_distance, graph[i][j])

print(max_distance)
