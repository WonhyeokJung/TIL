T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print("#{}".format(tc))

    arr = [[]*i for i in range(N)]

    for i in range(N):
        for j in range(i, N):
            arr[N-i-1].append(1)

    for i in range(len(arr)):
        for j in range(1, len(arr[i])-1):
            if i >= 2:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        print(*arr[i])


