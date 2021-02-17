T = int(input())

num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T+1):
    test_case, n = input().split()
    n = int(n)
    print(n)
    num_input = list(input().split())

    result = []

    for i in range(len(num_list)):
        for j in range(n):
            if num_list[i] == num_input[j]:
                result.append(num_list[i])

    print("#{}".format(tc), end=" ")
    print(*result)