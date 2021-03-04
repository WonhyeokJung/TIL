# def dfs(array, y):
#     global cnt, min_cnt
#     # y에서 갈수 있는 길이 있는 지 확인
#     for k in range(len(array[y])):
#         if array[y][k] == 1:
#             cnt += 1
#             array[y][k] = 0
#             array[k][y] = 0
#             # 도착했다면
#             if k == G:
#                 if min_cnt > cnt:
#                     min_cnt = cnt
#             dfs(array, k)
#             array[y][k] = 1
#             array[k][y] = 1
#     cnt -= 1

def bfs(graph, start_point, num):
    global cnt # cnt값 변경 위함
    queue = []
    visited = [False] * (num + 1)  # 0번 안씀
    queue.append(start_point)
    while queue:
        semi_queue = []
        while queue:
            current = queue.pop(0)  # 가장 위의 정점 뽑아오기
            if not visited[current]:  # 방문하지 않은 곳이라면
                visited[current] = True
            for k in range(len(graph[current])):  # 현재 정점과 연결된 정점들
                if graph[current][k] == 1 and k == G:
                    cnt += 1
                    return cnt
                if graph[current][k] == 1 and not visited[k]:  # 연결된 간선이 있다면
                    semi_queue.append(k)
        cnt += 1
        queue = semi_queue
    # 큐가 다비었다면 그때까지 도착을 못한 것
    cnt = 0
    return 0


T = int(input())

for tc in range(1, T + 1):
    # 노드수, 간선수
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    # 최소거리 카운트
    cnt = 0

    # 최소거리 조정
    min_cnt = 10000

    for _ in range(M):
        i, j = map(int, input().split())
        arr[i][j] = 1
        arr[j][i] = 1

    S, G = map(int, input().split())
    bfs(arr, S, N)
    print("#{} {}".format(tc, cnt))