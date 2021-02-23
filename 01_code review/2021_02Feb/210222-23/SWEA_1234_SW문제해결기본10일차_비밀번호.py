# 돌면서 붙은 숫자 제거하기
T = 10

for tc in range(1, T+1):
    # 문자열 길이와 그 문자
    N, text = input().split()
    N = int(N)
    arr = []
    for i in range(len(text)):
        arr += [text[i]]

    isFalse = True
    while isFalse:
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                arr.pop(i)
                arr.pop(i)
                break
        else:
            isFalse = False
    print("#{}".format(tc), end=" ")
    for i in range(len(arr)):
        print(arr[i], end="")
    print()

