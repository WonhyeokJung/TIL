# dfs 함수 정점과 간선의 인접리스트 graph, 현재 위치 n, 방문한 곳 T/F배열 visited
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
# 정점수보다 하나 많은 array (Index는 0부터 시작이지만, n 시작점(시작 정점)이 1이어서 맞춰주려고
arr = [[] for _ in range(N+1)]

# 간선수만큼 돌면서
for i in range(M):
    # 간선을 2차원의 인접리스트에 각각 배치한다.
    j, k = map(int, input().split())
    arr[j].append(k)
    arr[k].append(j)  # 유향이면 생략가능하다.

visited = [False]*(N+1)

dfs(arr, 1, visited)
