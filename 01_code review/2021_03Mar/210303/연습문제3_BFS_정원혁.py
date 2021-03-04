# 정점수, 간선수
# 모든간선
"""
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
"""


# 그래프와 시작점, 정점 수
def BFS(graph, start_point, num):
    queue = []
    visited = [False] * (num + 1)  # 0번 안씀
    queue.append(start_point)
    while queue:
        current = queue.pop(0)  # 가장 위의 정점 뽑아오기
        if not visited[current]:  # 방문하지 않은 곳이라면
            visited[current] = True
            print(current, end=" ")
        for k in range(len(graph[current])):  # 현재 정점과 연결된 정점들
            if graph[current][k] == 1 and not visited[k]:  # 연결된 간선이 있다면
                queue.append(k)
    return "<- 출력순서"


N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]  # Index 편의 위함
for _ in range(M):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1

print(BFS(arr, 1, N))
