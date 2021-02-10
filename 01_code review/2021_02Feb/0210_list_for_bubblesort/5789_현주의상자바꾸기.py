# Test Case
tc = int(input())

for t in range(tc):
    N, Q = map(int, input().split())

    # 숫자 0이 써있는 박스 N개
    boxes = [0]*N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        while L <= R:
            boxes[L-1] = i
            L += 1

    print("#{}".format(t + 1), end=" ")
    for result in range(N-1):
        print("{}".format(boxes[result]), end=" ")
    print("{}".format(boxes[N-1]))
