def dfs(arr, y, x):
    global check
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
                check = 1
            elif arr[r][c] == 0 and visited[r][c] == 0:
                visited[r][c] = 1
                dfs(arr, r, c)
        r -= dy[k]
        c -= dx[k]
    return check


for t in range(1, 11):
    # 테스트케이스
    tc = int(input())
    # 미궁
    labyrinth = [[int(i) for i in input()] for _ in range(16)]
    # 결과 담을 result
    result = []
    # 3에 도달했는지 체크
    check = 0
    # 방문했는가?
    visited = [[0]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if labyrinth[i][j] == 2:
                print("#{} {}".format(tc, dfs(labyrinth, i, j)))
                break