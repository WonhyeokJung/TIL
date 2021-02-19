import sys

sys.stdin = open("1216_input.txt", "r")

# zip까지 활용할 경우
def my_find2(M):
    for i in range(N):
        for j in range(N-M+1):
            tmp = words[i][j:j+M]
            tmp2 = zwords[i][j:j+M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M
    return 0

def my_find(M):
    # 전체 크기가 N이다.
    for i in range(N):

        # 부분 문자열의 시작점. 회문의 길이 M
        for j in range(N-M+1):
            #Swap 응용 회문검사
            # 가로검사
            for k in range(M//2):
                # 앞뒤검사
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                #회문이다
                elif k == M//2 -1:
                    return M

            # 세로검사
            for k in range(M//2):
                if words[j+k][i] != words[j+M-1-k][i]:
                    break
                elif k == M//2 -1:
                    return M
    return 0

for tc in range(10):
    tc_num = int(input())

    N = 100

    words =[input() for i in range(N)]
    # zip 이용해서 열을 행으로 바꿈
    # zwords = list(zip(*words))

    # 가장 길이가 긴 회문부터 검사
    for i in range(N, 0, -1):
        ans = my_find(i)

        if ans != 0:
            break

    print("#{} {}".format(tc_num, ans))