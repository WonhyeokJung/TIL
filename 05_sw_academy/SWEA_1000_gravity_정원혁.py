total_cases = int(input())

for total_case in range(total_cases):
    width = int(input())
    boxes = list(map(int, input().split()))
    k_count = [0] * 100
    k = [0] * 100
    count = 0
    result = [0] * 100
    for i in range(100):
        for j in range(len(boxes)):
            if boxes[j] >= i + 1:
                k[i] = (j+1)
                break;

    for i in range(100):
        for j in range(len(boxes)):
            if boxes[j] >= i + 1:
                k_count[i] += 1

    for i in range(0,100):
        if not k[i] == 0:
            # 여기를 width로 하면 7 6 13이 나옴
            result[i] = 100 - k_count[i] - k[i] + 1

    for i in range(0, 99):
        if result[i] > result[i+1]:
            result[i], result[i+1] = result[i+1], result[i]

    print("#{} {}".format(total_case + 1,result[len(result)-1]))

