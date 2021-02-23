T = int(input())

for tc in range(1, T+1):
    arr = []
    text = input()
    for i in range(len(text)):
        arr.append(text[i])
    isFalse = True
    while isFalse:
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                arr.pop(i)
                arr.pop(i)  # i+1이 i 자리로 이동했음
                break
        else:
            isFalse = False

    print("#{} {}".format(tc, len(arr)))


