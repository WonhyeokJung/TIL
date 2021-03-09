T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    W = [0]*N
    B = [0]*N
    R = [0]*N

    for i in range(N):
        for j in range(M):
            if arr[i][j] != "W":
                W[i] += 1
            if arr[i][j] != "B":
                B[i] += 1
            if arr[i][j] != "R":
                R[i] += 1

    for i in range(1, N):
        W[i] += W[i-1]
        B[i] += B[i - 1]
        R[i] += R[i - 1]


    result = 987654321

    for i in range(N-2):
        sum = 0
        for j in range(i+1,N-1):
            sum = W[i] + B[j] - B[i] + R[N-1] - R[j]
            if sum < result:
                result = sum

    print("#{} {}".format(tc, result))