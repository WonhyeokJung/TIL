def minsur(col):
    # 현재값 sumr, 최소값 minr
    global sumr, minr
    
    if minr < sumr:
        return

    elif col == N:
        if sumr < minr:
            minr = sumr
        return
        
    for j in range(N):
        # 방문한 열이 아니라면
        if not visited_c[j]:
            visited_c[j] = True
            sumr += arr[col][j]
            # 다음열 찾기
            minsur(col+1)
            visited_c[j] = False
            sumr -= arr[col][j]


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[int(i) for i in input().split()] for _ in range(N)]
    visited_c = [False]*N
    sumr, minr = 0, 999999999
    # 0번 열부터 시작
    minsur(0)
    print("#{} {}".format(tc, minr))


"""
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

output
#1 8
#2 14
#3 9
"""