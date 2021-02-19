T = int(input())

for tc in range(1, T+1):
    pattern = input()
    text = input()
    count_list = [0]*len(pattern)

    # pattern_dict = {}
    # for i in range(len(pattern)):
    #     pattern_dict[i] = pattern[i]

    for i in range(len(pattern)):
        for j in range(len(text)):
            if pattern[i] == text[j]:
                count_list[i] += 1

    max = 0
    for i in count_list:
        if i > max:
            max = i

    print("#{} {}".format(tc, max))

