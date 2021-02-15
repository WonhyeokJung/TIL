# 상하좌우로 인접한 항들 더한 절대값들을, 모든 원소 별로 다 구하여 전부 합한 결과를 Return하기 
import random

def absolute_value(n):
    if n < 0:
        return -n
    else:
        return n
    
# 재미로 만들어본, 숫자 5개씩 임의로 들어간 array 만들기
imsi = []*5
print(imsi)
for m in range(5):
    imsi.append(random.sample(range(1,101), 6))
    print(imsi)


arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]
# 행의 길이
N = 5
# 상하좌우를 의미하는 delta x축과 delta y축
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
result = 0

# 행
for i in range(len(arr)):
    # 열
    for j in range(len(arr[i])):
        for k in range(4):
            # y축값은 행기준
            y = i + dy[k]
            # x축값은 열기준
            x = j + dx[k]

            if y < 0 or y >= N or x < 0 or x >= N: continue
            result += absolute_value(arr[i][j]- arr[y][x])
print(result)