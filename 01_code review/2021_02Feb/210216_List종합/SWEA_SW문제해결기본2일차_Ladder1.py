import sys

sys.stdin = open("input.txt", "r")


# 아래 지랄을 안하고, 양 옆에 1이 있으면 이동하고, 지나온 길을 0으로 만들면 훨씬 깔끔하게 할 수 있다.


# arr은 100*100 배열 xy_arr , x는 숫자가 2인 곳의 x좌표.
def delta_xy(arr, x):
    # 상좌우
    dy =[-1, 0, 0]
    dx =[0, -1, 1]
    # 상좌우 움직임 설정할 num
    num = 0

    # y는 현재 y좌표
    y = 99

    while y >= 0:
        y += dy[num]
        x += dx[num]
        if y == 0:
            return x

        # 기존에 상으로 가고있었을 때(num=0), 상값에 상관없이 좌우 확인
        if num == 0:
            # x+1이 100 이상일땐, 우측으로 진행을 막겠다.
            if x+1 >= 100:
                # x좌표가 0 넘으면서, 좌측이 1일때
                if 1 == arr[y][x-1] and x-1 >= 0:
                    num = 1
                else:
                    num = 0
            # x+1이 100 미만일때도 좌측으로 움직임이 가능한가 확인
            elif 1 == arr[y][x-1] and x-1 >= 0:
                num = 1

            # x-1이 0미만일 땐, 좌측으로 진행을 막는다.
            elif x-1 <= -1:
                # x좌표가 99 안넘으면서, 우측이 1일떄
                if arr[y][x+1] == 1 and x+1 <= 99:
                    num = 2
                else:
                    num = 0
            # x-1이 0 이상일때도, 우측으로 이동할 수 있는 지 확인
            elif arr[y][x+1] == 1 and x+1 <= 99:
                num = 2
            # 둘 다 조건을 만족 못했다면, 상으로 가자
            else:
                num = 0

        # 기존에 좌로 가고있었을 때, 우측은 따질 필요가 없음 이미 지나온 길이어서.
        elif num == 1:
            # x가 이미 0이라면 위로!
            if x == 0:
                num = 0
            # 좌측 x좌표 값이 0을 넘고, 그 값이 1이라면 num은 그대로 1
            elif arr[y][x-1] == 1 and x - 1 >= 0:
                num = 1
            # 아니라면 상으로
            else:
                num = 0
        # 기존에 우측으로 갔을 때, 좌측은 따질 필요가 없음 내가 지나온 길이라서
        elif num == 2:
            # 이미 99번이라면 바로 상으로
            if x == 99:
                num = 0
            elif arr[y][x+1] == 1 and x + 1 <= 99:
                num = 2
            else:
                num = 0
        else:
            num =  0
    return x


        # 기존에 우로 가고 있었을 때,


T = 10

for tc in range(1, T + 1):
    # 1~10
    tc = int(input())

    # 상좌우. 사다리 타고 올라가기 용
    dyx = [[-1, 0], [0, -1], [0, 1]]

    # 100*100 행렬
    xy_arr = []

    # 숫자 2의 X좌표
    X = 0

    # 각 행 받기
    for i in range(100):
        imsi_arr = list(map(int, input().split()))
        xy_arr.append(imsi_arr)

    # 2의 location 찾기
    for i in range(100):
        if xy_arr[99][i] == 2:
            X = i

    # xy_arr[99][X]부터 거꾸로 올라가면서, 좌우에 길이 있으면 그 방향으로 전환
    print("#{} {}".format(tc, delta_xy(xy_arr, X)))


