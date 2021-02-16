# Test case
T = int(input())

for tc in range(1, T + 1):
    # 정수의 개수
    N = int(input())
    # 실제 정수
    arr = list(map(int, input().split()))
    # 가장 큰 수, 가장 작은 수, 두번째 큰수, 두번째 작은 수 순으로 10개 담을 List
    result = []
    # Bubble Sort
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    # 총 10개 넣어야 하니 절반인 5번만
    for i in range(0, 10 // 2, 1):
        result.append(arr[len(arr) - 1 - i])
        result.append(arr[i])

    print("#{}".format(tc), end=" ")
    for i in range(len(result)):
        print(result[i], end=" ")
    print()
