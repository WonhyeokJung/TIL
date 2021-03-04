T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    arr = [(i, a[i]) for i in range(len(a))]


    # N 사이즈 화덕
    oven = []
    # 화덕에 넣기
    for i in range(N):
        oven.append(arr.pop(0))

    while len(oven) > 1:
        # 맨 앞에 것을 n//2 후 뒤로 넣어준다.
        pizza = oven.pop(0)
        oven.append((pizza[0], pizza[1]//2))

        # 0이 된 것이 있다면 꺼내주기
        if oven[len(oven)-1][1] <= 0:
            oven.pop()
            if len(arr) > 0:
                oven.append(arr.pop(0))

    print("#{} {}".format(tc, oven[0][0]+1))




