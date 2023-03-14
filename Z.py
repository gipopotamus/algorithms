n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    ans += sum(arr[i][i:])

print(ans)