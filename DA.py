def main():
    n, m = map(int, input().split())
    a = []
    ans = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        line = input().split()
        a.append(list(''.join(line)))

    for i in range(n):
        for j in range(m):
            if a[i][j] == "#":
                ans = ans + 1
                queue = []
                queue.append([i, j])
                head = 0
                tail = 1
                a[i][j] = "."

                while head < tail:
                    p = queue[head]
                    x, y = p[0], p[1]

                    for k in range(4):
                        x1 = x + dx[k]
                        y1 = y + dy[k]
                        if x1 >= 0 and x1 < n and y1 >= 0 and y1 < m and a[x1][y1] == "#":
                            queue.append([x1, y1])
                            a[x1][y1] = "."
                            tail = tail + 1
                    head = head + 1

    print(ans)



if __name__ == "__main__":
    main()