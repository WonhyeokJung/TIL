T = int(input())

for tc in range(1, T + 1):
    # N : 원소의 개수
    # M : 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    # 구간 시작점
    for i in range(N - M + 1):
        tmp = 0

        for j in range(M):
            tmp += nums[i + j]

        # for j in nums[i:i+M]:
        #     tmp += j

        # tmp = sum(nums[i:i+M])

        # 큰값 갱신
        if max_value < tmp:
            max_value = tmp

        # 작은 값 갱신
        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))
#############################################################################
T = int(input())

for tc in range(1, T + 1):
    # N : 원소의 개수
    # M : 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 중복된 연산을 피하자.....

    # 첫구간은 구해 놓자...
    tmp = 0
    for i in range(M):
        tmp += nums[i]

    max_value = tmp
    min_value = tmp

    for i in range(M, N):
        # 새로운 구간의 합을 아주아주아주 간단하게 구할수 있음
        tmp = tmp + nums[i] - nums[i - M]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))
