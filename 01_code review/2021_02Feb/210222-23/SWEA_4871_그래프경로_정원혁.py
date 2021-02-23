def dfs(s):
    visited[s] = True
    for i in range(V):
        if arr[s][i] and not visited[i]:
            dfs(i)


T = int(input())

for tc in range(1, T+1):
    # 정점수와 간선수
    V, E = map(int, input().split())
    # 정점수만큼 x,y 좌표를 갖는 2차원 배열(인접행렬이용)
    arr = [[0]*V for _ in range(V)]
    visited = [False]*V

    for i in range(E):
        y, x = map(int, input().split())
        arr[y-1][x-1] = 1
        # arr[x-1][y-1] = 1 # 유향 그래프면 생략가능
    # 경로는 존재하는가
    # Start Node S, 도착점 Goal G
    S, G = map(int, input().split())

    dfs(S-1)
    # visited[0] = 1번 node 방문했다는 의미
    if visited[G-1]:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))