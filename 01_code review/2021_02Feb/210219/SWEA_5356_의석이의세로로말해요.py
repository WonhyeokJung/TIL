T = int(input())

for tc in range(1, T+1):
    # 최대 문장 길이 15. 문장은 5줄씩
    test_str = [["xx"]*15 for _ in range(5)]
    
    # 반환할 결과값
    result =""
    # 텍스트 길이가 각각 다르므로 최대 텍스트 길이 담기
    text_leng = 0
    
    # 문장 수만큼 input 받아 각 항의 값 교체
    for i in range(len(test_str)):
        text = input()
        if len(text) > text_leng:
            text_leng = len(text)

        for j in range(len(text)):
            test_str[i][j] = text[j]

    # 출력 x값은 text최대길이만큼, y값은 test_str length, 즉 5줄씩
    for i in range(text_leng):
        for j in range(len(test_str)):

            if not test_str[j][i] == "xx":
                result += test_str[j][i]
    print("#{} {}".format(tc, result))