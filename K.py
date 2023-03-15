class Vertex:
    def __init__(self, color=0, coloring=0, cnt_in_comp=0):
        self.Color = color
        self.Coloring = coloring
        self.Cnt_in_comp = cnt_in_comp


class Graph:
    def __init__(self, adj_list):
        self.Adj_list = adj_list
        self.Data = [Vertex() for i in range(len(adj_list))]


def DFS(vertex, in_graph, flag, color_end):
    in_graph.Data[vertex].Color = 1
    for u in in_graph.Adj_list[vertex]:
        if in_graph.Data[u].Color == 0:
            color = in_graph.Data[vertex].Coloring + 1
            in_graph.Data[u].Coloring = (color % 2)
            DFS(u, in_graph, flag, color_end)
        else:
            if in_graph.Data[vertex].Coloring == in_graph.Data[u].Coloring:
                flag[0] = 1
    in_graph.Data[vertex].Color = 2
    color_end[0] = in_graph.Data[vertex].Coloring


if __name__ == "__main__":
    n, m = map(int, input().split())

    adj_list = [[] for i in range(n)]
    for i in range(m):
        vertex1, vertex2 = map(int, input().split())
        vertex1 -= 1
        vertex2 -= 1
        adj_list[vertex1].append(vertex2)
        adj_list[vertex2].append(vertex1)

    graph = Graph(adj_list)
    flag = [0]
    color_end = [0]

    for i in range(n):
        if graph.Data[i].Color == 0:
            graph.Data[i].Coloring = (color_end[0] + 1) % 2
            DFS(i, graph, flag, color_end)

    if flag[0] == 0:
        print("YES")
    else:
        print("NO")
