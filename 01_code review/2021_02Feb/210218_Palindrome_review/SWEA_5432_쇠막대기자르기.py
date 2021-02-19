T = int(input())

for tc in range(1, T + 1):
    # 레이저에 의해 잘릴 쇠막대기 수
    count = 0
    # 잘려서 나뉜 쇠막대기 총값
    result = 0
    # 쇠막대기 텍스트
    text = input()

    for i in range(0, len(text) - 1):
        # 쇠막대기 추가
        if text[i] == "(":
            count += 1
            # 붙어있음 레이저니까 count -1
            if text[i + 1] == ")":
                count -= 1
        if text[i] == ")":
            count -= 1
            # 앞에서 레이저로 판단해 count 뺏을테니 두번 빼는걸 막기 위함 + result에 잘린 쇠막대 숫자 더하기
            if text[i - 1] == "(":
                count += 1
                result += count
            else:
                result += 1
    # 마지막 돌지 않은 for 문에서 ))였으면 count가 1, ()면 count가 0이므로, count값을 마지막에 추가
    print("#{} {}".format(tc, result + count))
