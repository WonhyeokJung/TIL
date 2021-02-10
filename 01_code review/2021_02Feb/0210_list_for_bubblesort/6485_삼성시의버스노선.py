T = int(input())

for tc in range(1, T+1):
    # 총 버스 노선
    N = int(input())
    a_list = []
    b_list = []
    for i in range(N):
        # 두 정수 a, b
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    # 하나의 정수 p
    p = int(input())
    c_list = [0] * p
    for j in range(p):
        c = int(input())
        for k in range(N):
            if a_list[k] <= c <= b_list[k]:
                c_list[j] += 1

    print("#{}".format(tc), end=" ")
    for val in range(len(c_list)-1):
        print("{}".format(c_list[val]), end=" ")
    print("{}".format(c_list[len(c_list)-1]))

