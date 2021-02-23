# DP 예제

def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    else:
        return dp(n-1) + 2*dp(n-2)



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print("#{} {}".format(tc, dp(N//10)))
