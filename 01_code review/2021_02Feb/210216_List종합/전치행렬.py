# 가로순 행렬을, 세로순 행렬로 바꿔주는 방식.

# i = 행의 좌표
# j = 열의 좌표

arr = [[1,2,3], [4,5,6], [7,8,9]]  # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)