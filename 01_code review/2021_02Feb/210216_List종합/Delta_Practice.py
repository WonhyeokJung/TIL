# 상하좌우의 탐색

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 현재 서있는 위치 좌표
r = 0
c = 0
# 행의 길이
N = 3

# 상하좌우 dc, dr(column, row)로도 표현함
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# dxy = [[0,-1],[0,1][-1,0],[1,0]]

for i in range(4):
    ny = r + dy[i]
    nx = c + dx[i]

    # Python은 리스트 인덱스 -1이면 값을 가져오므로, 이런 위험을 없애기 위해 if문으로 제약조건.
    # 범위를 벗어나면 작업을 건너뛰기.
    if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
    print(arr[ny][nx])