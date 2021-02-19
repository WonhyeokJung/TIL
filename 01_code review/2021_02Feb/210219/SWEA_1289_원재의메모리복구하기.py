T = int(input())

for tc in range(1, T + 1):
    num_list = list(input())
    n = ['0'] * len(num_list)
    result = 0
    for i in range(len(n)):
        if n[i] != num_list[i]:
            n[i:] = num_list[i] * len(n[i:])
            result += 1

    print('#{} {}'.format(tc, result))

