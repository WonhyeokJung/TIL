# 우랑 하만 필요함. 다 사각형이니까
def dimensions(y, x):
    global row, column, arr
    # 우 하. 열먼저 검토한다. 행먼저 검토하는줄 개멍청함.
    dy = [0, 1]
    dx = [1, 0]

    r = y + dy[0]
    c = x + dx[0]
    # 열 먼저 검토 후 다음 행 검토
    for k in range(2):
        while 0 <= r < N and 0 <= c < N and arr[r][c] != 0:
            if k == 0:
                column += 1
            else:
                row += 1
            r += dy[k]
            c += dx[k]
        # while문을 못돌았다면 원래좌표에서 계산을 해야하므로.
        # 이거 때문에 row는 한번씩 더 돌게됨 ㅋㅋ...
        else:
            r -= dy[k]
            c -= dx[k]
    result.append([column*(row-1), row-1, column])
    column = 1
    row = 1
    # r까지 0으로
    for l in range(y, r+1):
        # c까지 0으로
        for m in range(x, c+1):
            arr[l][m] = 0
    return


T = int(input())

for tc in range(1, T+1):
    # arr 크기 N*N
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 기본 가로 길이 1
    row = 1
    # 기본 세로 길이 1
    column = 1

    result = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                dimensions(i, j)

    for i in range(len(result)-1):
        for j in range(i+1, len(result)):
            if result[i][0] > result[j][0]:
                result[i], result[j] = result[j], result[i]
            # 크기가 같은 경우 행이 작은 순으로
            if result[i][0] == result[j][0]:
                if result[i][1] > result[j][1]:
                    result[i], result[j] = result[j], result[i]

    # 출력은 tc, 총 사각형 개수, 사이즈 작은 순으로 행, 열 출력.
    print("#{} {}".format(tc, len(result)), end=" ")
    for i in range(len(result)):
        print("{} {} ".format(result[i][1], result[i][2]), end="")
    if tc != len(result):
        print()

