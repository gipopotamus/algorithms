def main():
    n, m = map(int, input().split())
    count = 0

    b = []
    c = []
    a = []
    for i in range(n):
        a.append(0)
        b.append(i + 1)

    for i in range(m):
        u, v = map(int, input().split())
        c.append(u)
        c.append(v)
    for i in range(n):
        for j in range(len(c)):
            if c[j] == b[i]:
                a[i] = a[i] + 1

    ans = ' '.join([str(x) for x in a])
    print(ans, sep='\n')


if __name__ == "__main__":
    main()