T = int(input())

# 테스트 케이스 먼저 출력
for tc in range(1, T+1):
    # 횟수
    N = int(input())
    print("#{}".format(tc))

    # 2차원 배열의 생성
    arr = [[] for i in range(N)]
    # n번만큼 돌면서
    for i in range(N):
        # 1을 n번째엔 n개, n-1번째엔 n-1개씩을 넣어준다.
        for j in range(i, N):
            arr[N-i-1].append(1)

    # arr 길이(n)만큼 돌면서
    for i in range(len(arr)):
        for j in range(1, len(arr[i])-1):
            # 행수가 2행 이상이라면,
            if i >= 2:
                # 윗행의 두 값을 더한만큼으로 값을 바꿔줍니다.
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        # 출력
        print(*arr[i])

""" 출력 예시
N = 4
   1
  1 1
 1 2 1
1 3 3 1
"""


