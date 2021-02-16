# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 영역 칠할 횟수
    N = int(input())

    # 붉은색 범위와 파란색 범위 담을 array
    red_arr = []
    blue_arr = []
    
    # 영역 칠할 횟수만큼 돌면서
    for i in range(N):
        # 좌표, 좌표, 색상
        y1, x1, y2, x2, color = map(int, input().split())

        # 결과값 담을 count
        count = 0

        # 붉은색은 red_arr에
        if color == 1:
            for j in range(x1, x2+1):
                for k in range(y1, y2+1):
                    # y축부터 숫자 넣어야 함에 유의(컴퓨터는 행부터 읽음)
                    red_arr.append([k, j])

        # 파란색(2)은 blue_arr에 담는다.
        if color == 2:
            for j in range(x1, x2+1):
                for k in range(y1, y2+1):
                    # y축부터 숫자 넣어야 함에 유의(컴퓨터는 행부터 읽음)
                    blue_arr.append([k, j])

        # 두 Array 비교하여 중복값있으면 count +1
        for k in red_arr:
            for l in blue_arr:
                if k == l:
                    count += 1
    # 결과 출력은 Case당 한번
    print("#{} {}".format(tc, count))