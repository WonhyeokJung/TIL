T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    for i in range(N-1):
        min = i
        for j in range(i+1, N):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    print("#{}".format(tc), end=" ")
    for i in range(len(arr)):
        print("{}".format(arr[i]), end=" ")
    print()
    # print(*arr, end=" ")
