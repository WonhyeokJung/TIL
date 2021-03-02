def dfs(array, start_y, start_x):
    r = start_y
    c = start_x
    # 상우하좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    # 전역변수 result를 사용하겠다. 여기 result를 0으로 준다면, 계속 초기화해서 return이 0으로 가게 된다.
    global result
    # 이동 가능한곳 체크하며 이동
    for i in range(4):
        r += dy[i]
        c += dx[i]
        if 0 <= r <= len(array)-1 and 0 <= c <= len(array)-1:
            if array[r][c] == 3:
                # dfs중간에 이것이 실행됐다면, 그 이후로 보이지 않는 return은 계속 "#{tc} 1"로 이뤄지고 있을 것이다.
                result = 1
            elif array[r][c] == 0 and visited[r][c] == 0:
                visited[r][c] = 1
                # return은 지속적으로 이뤄지나, 내가 이 return을 print하지 않아서, print 값은 41행 단 한번만 나온다.
                # 내가 보지 못하는 것뿐, return은 계속 하고 있다.
                dfs(arr, r, c)
        # 위에 조건에 부합하지 않았다면 다시 그 값에서 돌아야하니까
        r -= dy[i]
        c -= dx[i]

    return "#{} {}".format(tc, result)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 공백없이 입력된 한줄의 str을 하나씩 분리해 넣어주는 이차원 배열 생성
    arr = [[int(i) for i in input()] for _ in range(N)]
    # visited가 없다면, 본인이 왔던 곳도 다시 돌아가서 무한으로 도는 문제가 생긴다.
    visited = [[0]*N for _ in range(N)]
    # 미로를 탈출하면 값이 1로 변한다
    result = 0
    for a in range(N):
        for z in range(N):
            # 마지막줄의 2번이 출발점
            if arr[a][z] == 2:
                print(dfs(arr, a, z))