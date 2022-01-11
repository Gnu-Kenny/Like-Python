graph = []
visited = []


def dfs(graph, now, visited):
    visited[now] = True
    for node in graph[now]:
        if visited[node] == True:
            continue
        dfs(graph, node, visited)


def main():
    node_num = int(input())
    edge_num = int(input())

    visited = [False for _ in range(node_num + 1)]
    graph = [
        [] for _ in range(node_num + 1)
    ]  # node_num+1 => graph의 index와 노드의 값을 동일하게 하기 위해

    # 인접 행렬 내부 요소들을 정렬해줘야할때도 있나?
    for _ in range(edge_num):
        v = list(map(int, input().split()))
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    dfs(graph, 1, visited)
    print(visited)
    print(visited.count(True) - 1)


if __name__ == "__main__":
    main()
