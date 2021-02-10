T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    # 임시 최대값. 음의 정수도 list 내 있으므로, 음수값이 최대값일 경우를 고려해서.
    max_sum = -987654321
    result = []
    if N > M:
        # 더 작은 Array의 위치를 하나씩 옮기기
        for i in range(N - M + 1):
            # 곱하고 더한 값 저장할 sums 초기화
            sums = 0
            for j in range(len(M_list)):
                sums += N_list[i + j] * M_list[j]
            result.append(sums)

    elif N < M:
        for i in range(M - N + 1):
            sums = 0
            for j in range(len(N_list)):
                sums += N_list[j] * M_list[j + i]
            result.append(sums)

    for i in result:
        if i > max_sum:
            max_sum = i

    print("#{} {}".format(t + 1, max_sum))
