def recursive(a, b):
    if b == 1:
        return a
    if b%2 == 0:
        y = recursive(a, b//2)
        return y*y
    else:
        y = recursive(a, (b-1)//2)
        return y*y*a  # 하나 따로 곱해주기

for tc in range(1, 11):
    N = int(input())
    M, O = map(int, input().split())

    print("#{} {}".format(tc, recursive(M, O)))