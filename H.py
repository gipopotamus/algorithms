from collections import deque

n, m = (int(s) for s in input().split())
labyrinth = [0] * (n + 2)
for i in range(1, n + 1):
    labyrinth[i] = [1] + [int(s) for s in input().split()] + [1]
labyrinth[0] = labyrinth[n + 1] = [1] * (m + 2)
start = (1, 1)
visited = {start: 0}
queue = deque([start])
while queue:
    cur_row, cur_column = queue.popleft()

    for i in range(1, m + 2):
        next_row, next_column = cur_row, cur_column + i

        if labyrinth[next_row][next_column] == 2:
            print(visited[(cur_row, cur_column)] + 1)
            exit()
        elif labyrinth[next_row][next_column] == 1:
            if (next_row, next_column - 1) not in visited:
                visited[(next_row, next_column - 1)] = visited[(cur_row, cur_column)] + 1
                queue.append((next_row, next_column - 1))
                break
            else:
                break

    for i in range(1, m + 2):
        next_row, next_column = cur_row, cur_column - i

        if labyrinth[next_row][next_column] == 2:
            print(visited[(cur_row, cur_column)] + 1)
            exit()
        elif labyrinth[next_row][next_column] == 1:
            if (next_row, next_column + 1) not in visited:
                visited[(next_row, next_column + 1)] = visited[(cur_row, cur_column)] + 1
                queue.append((next_row, next_column + 1))
                break
            else:
                break

    for i in range(1, n + 2):
        next_row, next_column = cur_row - i, cur_column

        if labyrinth[next_row][next_column] == 2:
            print(visited[(cur_row, cur_column)] + 1)
            exit()

        elif labyrinth[next_row][next_column] == 1:
            if (next_row + 1, next_column) not in visited:
                visited[(next_row + 1, next_column)] = visited[(cur_row, cur_column)] + 1
                queue.append((next_row + 1, next_column))
                break
            else:
                break

    for i in range(1, n + 2):
        next_row, next_column = cur_row + i, cur_column

        if labyrinth[next_row][next_column] == 2:
            print(visited[(cur_row, cur_column)] + 1)
            exit()

        elif labyrinth[next_row][next_column] == 1:
            if (next_row - 1, next_column) not in visited:
                visited[(next_row - 1, next_column)] = visited[(cur_row, cur_column)] + 1
                queue.append((next_row - 1, next_column))
                break
            else:
                break