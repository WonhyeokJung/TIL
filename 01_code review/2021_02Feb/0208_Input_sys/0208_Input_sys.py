# Ssafy 1206번 D3 View(조망권 문제)

# txt파일을 읽어올 수 있는 sys를 import
import sys
#r은 read, 읽어오기를 의미
sys.stdin = open("input.txt", "r")
#for문을 돌며 (input.txt의 Total case가 10개였기때문에, 1~11로 잡았다.
for tc in range(1, 11):
    x = int(input())
    # input을 공백기준으로 자르고, int로 변환 후 list에 넣는 box 변수 선언
    box = list(map(int, input().split()))
    # 결과 담을 것.
    result = 0
    if x <= 1000:
        for i in range(2, x-2):
            # 좌우 간격 2칸 내의 빌딩 중 최고높이를 찾고,
            max_height = max([box[i-2],box[i-1],box[i+1],box[i+2]])
            if box[i] > max_height:
                # 결과값을 도출한다.
                result += box[i] - max_height
    # fstring의 또 다른 형태 format을 사용
    print("#{} {}".format(tc, result))