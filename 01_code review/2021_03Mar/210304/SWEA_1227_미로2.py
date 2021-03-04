def dfs(arr, y, x):
    global queue, check
    # 상우하좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    queue.append(y)
    queue.append(x)
    while queue:
        r = queue.pop(0)
        c = queue.pop(0)
        arr[r][c] = 1
        for k in range(4):
            r += dy[k]
            c += dx[k]
            if 0 <= r < len(arr) and 0 <= c < len(arr):
                if arr[r][c] == 3:
                    check = 1
                    return check
                elif arr[r][c] == 0:
                    queue.append(r)
                    queue.append(c)

            r -= dy[k]
            c -= dx[k]
    return check

for t in range(1, 11):
    # 테스트케이스
    tc = int(input())
    # 미궁
    labyrinth = [[int(i) for i in input()] for _ in range(100)]
    # Queue
    queue = []
    # 3에 도달했는지 체크
    check = 0
    # 방문했는가?
    for i in range(100):
        for j in range(100):
            if labyrinth[i][j] == 2:
                print("#{} {}".format(tc, dfs(labyrinth, i, j)))
                break