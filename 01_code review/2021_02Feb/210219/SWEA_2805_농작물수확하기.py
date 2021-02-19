T = int(input())

for tc in range(1, + T+1):
    n = int(input())
    test_list = [list(map(int,input())) for _ in range(n)]

    if n == 1:
        result = test_list[0][0]

    else:

        result = 0
        j = n
        while j > 0:
            for i in range(n//2, 0, -1):
                for k in range(j):
                    result += test_list[i][k]
                j -= 2

        j = n - 2
        while j > 0:
            for i in range(n//2 + 1, n):
                for k in range(j):
                    result += test_list[i][k]
                j -= 2

    print("#{} {}".format(tc, result))
