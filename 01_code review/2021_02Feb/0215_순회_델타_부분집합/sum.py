import sys
# 텍스트 문서를 받아와 봅시다.
sys.stdin = open("sum.txt", "r")

T = 10  # 테스트 케이스

for i in range(1, T + 1):
    # 각 행마다 tc 번호가 주어짐
    tc = int(input())
    # 최댓값
    max = 0
    # 비교할 imsi_max
    imsi_max = 0
    # 100x100 사이즈라고 문제에 주어져서, range는 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 대각선 놈들부터
    for j in range(100):
        max += arr[j][j]
        imsi_max += arr[j][99 - j]

    if max < imsi_max:
        max = imsi_max

    for k in range(100):
        # imsi_max의 재활용
        imsi_max = 0
        for l in range(100):
            imsi_max += arr[k][l]
        if imsi_max > max:
            max = imsi_max

    for k in range(100):
        # imsi_max의 재활용
        imsi_max = 0
        for l in range(100):
            imsi_max += arr[l][k]
        if imsi_max > max:
            max = imsi_max

    print("#{} {}".format(i, max))