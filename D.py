n = int(input())
parents = {}
heights = {}

for i in range(n - 1):
    child, parent = input().split()
    parents[child] = parent

for node in sorted(parents.keys()):
    if node not in heights:
        height = 0
        current_node = node
        while current_node in parents:
            current_node = parents[current_node]
            height += 1
            if current_node in heights:
                height += heights[current_node]
                break
        heights[node] = height
for i in parents.values():
    print(i)
    if i not in heights:
        heights[i] = 0
for node in sorted(heights.keys()):
    print(node, heights[node])