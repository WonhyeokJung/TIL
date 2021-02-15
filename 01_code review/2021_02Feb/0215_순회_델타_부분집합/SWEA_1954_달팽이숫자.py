T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 정사각형 구조 필요하므로
    result = [[0] * N for _ in range(N)]

    # 우하좌상의 순서
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    num = 0

    x = y = 0
    result[x][y] = 1

    for i in range(2, N ** 2 + 1):
        y += dy[num]
        x += dx[num]
        result[y][x] = i

        # 다음 좌표의 x,y 값이 4보다 작은지 + 다음 위치에 이미 값이 존재하는 지.
        if x + dx[num] < N and y + dy[num] < N and result[y + dy[num]][x + dx[num]] == 0:
            continue

        if not num == 3:
            num += 1
        # num이 3이라면 다시 0으로
        else:
            num = 0
    print("#{}".format(tc))
    for l in range(len(result)):
        for m in range(len(result[l])):
            print("{}".format(result[l][m]), end=" ")
        print()