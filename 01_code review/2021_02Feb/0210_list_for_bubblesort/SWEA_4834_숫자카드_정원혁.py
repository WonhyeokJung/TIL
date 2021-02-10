T = int(input())

for i in range(1,T+1):
    N = int(input())
    num = list(map(int,input()))
    check_list = [0]*10
    result = 0

    for j in num:
        check_list[j] += 1

    for k in range(len(check_list)-1,-1,-1):
        if check_list[k] > result:
            max_num = k
            result = check_list[k]
    print("#{} {} {}".format(i, max_num, result))