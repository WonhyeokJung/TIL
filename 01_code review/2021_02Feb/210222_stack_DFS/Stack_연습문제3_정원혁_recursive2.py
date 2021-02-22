# dfs 함수 정점과 간선 2차원리스트 graph, 현재 위치 n, 방문한 곳 TF배열 visited
def dfs(graph, n, visited):
    visited[n] = True
    print(n, end=" ")

    # graph[n]의 요소를 돌며
    for i in graph[n]:
        # 방문한 곳이 아니라면
        if not visited[i]:
            # 함수를 실행, 이 함수는 종료되지 않고 기다리고 있다가 다른 함수가 종료되면 또 실행된다.
            # Return문은 기존 함수가 정지되므로, 돌아갈 곳이 없어지면 진행이 불가능하다.
            dfs(graph, i, visited)

# 정점수, 간선수
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    j, k = map(int, input().split())
    arr[j].append(k)
    arr[k].append(j)

visited = [False]*(N+1)

dfs(arr, 1, visited)
