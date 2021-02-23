for tc in range(1, 11):
    N = int(input())
    test_case = input()
    arr = []
    for i in range(len(test_case)):
        arr.append(test_case[i])

    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0

    for i in arr:
        if i == "(":
            t1 += 1
        elif i == ")":
            t1 -= 1
        elif i == "{":
            t2 += 1
        elif i == "}":
            t2 -= 1
        elif i == "[":
            t3 += 1
        elif i == "]":
            t3 -= 1
        elif i == "<":
            t4 += 1
        elif i == ">":
            t4 -= 1


    if t1 == t2 == t3 == t4 == 0:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))
