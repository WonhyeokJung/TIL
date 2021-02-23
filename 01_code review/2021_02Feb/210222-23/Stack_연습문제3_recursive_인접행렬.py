# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
# 답 : 1 2 4 6 5 7 3 A B D F E G C
def dfs(n):
    visited[n] = True
    print(chr(n + 65), end=" ")  # A~Z로 정점이 명명되어 있다면..

    for i in range(N):
        if arr[n][i] and not visited[i]:
            dfs(i)


# 정점수, 간선수
N, M = map(int, input().split())

arr = [[0] *N for _ in range(N)]
visited = [False] * N
for i in range(M):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1
    arr[x-1][y-1] = 1  # 유향 그래프(방향이 정해져 있는 그래프)의 경우 필요없음.

# 1번 node가 0번이므로 0 투입
dfs(0)

########################################################
# 인덱스를 좀 더 편하게 사용해보자
def dfs2(n):
    visited[n] = True
    print(chr(n + 64), end=" ")

    for i in range(N+1):
        if arr[n][i] and not visited[i]:
            dfs2(i)

N, M = map(int, input().split())

# Index의 편의를 위해서
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    y, x = map(int, input().split())
    arr[y][x] = 1
    arr[x][y] = 1

for i in arr:
    print(*i)

# 1번 노드가 이젠 1번이니까..
dfs2(1)