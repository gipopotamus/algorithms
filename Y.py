def main():
    n = int(input())

    b = [list(input().split()) for i in range(n)]
    count = 1
    y = input()
    a = input().split()
    for i in range(n):
        for j in range(n):
            if b[i][j] == str(1) and a[i] != a[j]:
                count += 1
    ans = count // 2
    print(ans)


if __name__ == "__main__":
    main()