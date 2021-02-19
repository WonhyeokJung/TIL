# 길이가 M인 회문찾기

def palindrome(text, palindrome_len):
    result = ""
    for i in range(palindrome_len-1, -1, -1):
        result += text[i]
    if result == text:
        return result
    else:
        pass


T = int(input())
for tc in range(1, T+1):
    # N*N 크기의 문장표, 회문길이 M
    n, m = map(int, input().split())
    n_table = [[]*n for _ in range(n)]

    # 문장 수 만큼 돌면서...문자 들어간 2차원 배열 만들기
    for i in range(n):
        # 2차원 배열 만들어 문자 넣기
        a = input()
        for j in range(len(a)):
            n_table[i].append(a[j])

    # 문장 길이만큼 돌면서 회문을 찾기(행우선)
    for i in range(n):
        for j in range(0, n-m+1):
            row_sentence = ""
            column_sentence = ""
            # 행 돌면서 다 출력
            for k in range(j, j+m):
                row_sentence += n_table[i][k]
                column_sentence += n_table[k][i]

            if palindrome(row_sentence, m) != None:
               print("#{} {}".format(tc, palindrome(row_sentence, m)))
            if palindrome(column_sentence, m) != None:
               print("#{} {}".format(tc, palindrome(column_sentence, m)))

