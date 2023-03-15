n = int(input())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

s = -1
for i in range(n):
    for a in range(i + 1, n):
        for b in range(a + 1, n):
            if s == -1:
                s = arr[i][a] + arr[i][b] + arr[a][b]
                x, y, z = i + 1, a + 1, b + 1
            elif s > arr[i][a] + arr[i][b] + arr[a][b]:
                s = arr[i][a] + arr[i][b] + arr[a][b]
                x, y, z = i + 1, a + 1, b + 1

print(x, y, z)
