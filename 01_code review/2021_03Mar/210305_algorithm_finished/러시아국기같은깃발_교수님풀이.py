def perm(idx, sub_sum):
    global ans
    # 유망성 검사 아래의 조건문에 걸리게 되면
    # 이후 작업은 의미가 없음
    # sub_sum = 몇줄을 뽑았는가
    if sub_sum > N:
        return

    if idx == 3:
        if sub_sum == N:
            cnt = 0

            st = sel[0]  # 하얀색으로 채울 index
            st2 = st + sel[1]  # 하얀색 기준점 + 파란색 기준 Index

            # 흰색 칠하기
            for i in flag[:st]: # sel = [1, 3, 5]라면 흰색한줄, 파란색 3줄, 빨간색 한줄이 된다.
                for j in i:
                    if j != 'W':
                        cnt += 1

            # 파란색 칠하기
            for i in flag[st:st2]:
                for j in i:
                    if j != "B":
                        cnt += 1

            # 빨강색 칠하기
            for i in flag[st2:]:
                for j in i:
                    if j != "R":
                        cnt += 1

            if ans > cnt:
                ans = cnt
        return

    # 중복순열 살짝 응용
    for i in range(1, N-1):
        sel[idx] = i
        perm(idx+1, sub_sum + i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    flag = [list(input()) for _ in range(N)]
    sel = [0] * 3
    ans = 987654321

    # 앞에는 idx, 뒤에는 중간 합
    perm(0, 0)

    print("#{} {}".format(tc, ans))


##############################################

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    flag = [input() for _ in range(N)]

    W = [0] * N
    B = [0] * N
    R = [0] * N

    # 행을 보면서 나와 다른 색깔의 개수를 카운팅
    for i in range(N):
        for j in range(M):
            if flag[i][j] != "W":
                W[i] += 1
            if flag[i][j] != "B":
                B[i] += 1
            if flag[i][j] != "R":
                R[i] += 1
    # 각 항에 앞 값을 누적시키자(자기 색이 되려면 몇개나 바꿔야 하는지)
    for i in range(1, N):
        W[i] += W[i-1]
        B[i] += B[i-1]
        R[i] += R[i-1]

    ans = 987654321

    # 각 색은 한줄씩 확보를 해야하기 때문에
    for i in range(N-2):
        for j in range(i+1, N-1):
            w_cnt = W[i]
            b_cnt = B[j] - B[i]  # i까지는 흰색을 칠했으니까
            r_cnt = R[N-1] - R[j]

            if ans > w_cnt + b_cnt + r_cnt:
                ans = w_cnt + b_cnt + r_cnt

    print("#{} {}".format(tc, ans))