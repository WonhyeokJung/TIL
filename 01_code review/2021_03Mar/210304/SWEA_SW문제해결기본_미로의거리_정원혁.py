def dfs(arr, y, x):
    r = y
    c = x
    # 상우하좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    global result, check

    for k in range(4):
        r += dy[k]
        c += dx[k]
        if 0 <= r < len(arr) and 0 <= c < len(arr):
            if arr[r][c] == 3:
                check = -1
                print("#{} {}".format(tc, len(result)))
            elif arr[r][c] == 0 and visited[r][c] == 0:
                visited[r][c] = 1
                result += [(r, c)]
                dfs(arr, r, c)
        r -= dy[k]
        c -= dx[k]
    # 다 돌았다는 것은, 길이 막혔다는 것 or 이미 다녀온 길이므로 결과 Stack에서 -1씩 해준다.
    if len(result) >= 1:
        result.pop()


T = int(input())

for tc in range(1, T+1):
    # 미로 사이즈
    N = int(input())
    labyrinth = [[int(i) for i in input()] for _ in range(N)]
    # 결과 담을 result
    result = []
    # 3에 도달했는지 체크
    check = 0
    # 방문했는가?
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if labyrinth[i][j] == 2:
                dfs(labyrinth, i, j)
                break
    if check == 0:
        print("#{} {}".format(tc, len(result)))