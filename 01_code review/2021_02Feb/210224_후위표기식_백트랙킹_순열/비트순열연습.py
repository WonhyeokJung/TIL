# 집합
arr = [1, 2, 3]
# 3개씩 갖는 순열
N = 3

sel = [0] * N  # 뽑앗나 안뽑았나 확인


# 자리 컨트롤 idx, check라는 변수 // check 10진수 정수
def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for i in range(N):
        if check & (1 << i): continue  # 이미 값이 있으면 돌아가

        sel[idx] = arr[i]
        perm(idx + 1, check | (1 << i))  # 원상복귀 과정이 필요 X. 알아서 체크하므로


perm(0, 0)