def palindrome(text):
    result = ""
    for i in range(len(text)-1,-1,-1):
        result += text[i]
    if result == text:
        return len(text)

def count_length(str_list):
    # 회문 최대 길이 leng
    leng = 100
    # 가장 긴 것부터 회문검사
    while leng > 0:

        for y in range(100):  # 행길이
            for x in range(100 - leng + 1):  # 열 길이
                # 행 검사
                if palindrome(str_list[y][x:x + leng]) != None:
                    return palindrome(str_list[y][x:x + leng])
                # 열 기준 검사 (행과 열 반대로 입력)
                # 열 기준 문장
                column_sentence = ""

                for i in range(leng):
                    column_sentence += str_list[x + i][y]
                if palindrome(column_sentence) != None:
                    return palindrome(column_sentence)
        # 회문 길이를 하나씩 줄여나가며 회문길이 체크
        leng -= 1

T = 10
for tc in range(1, T+1):
    test_case = int(input())

    # str list 만들기
    str_list = []
    for i in range(100):
        str_list.append(input())


    print("#{} {}".format(tc, count_length(str_list)))







