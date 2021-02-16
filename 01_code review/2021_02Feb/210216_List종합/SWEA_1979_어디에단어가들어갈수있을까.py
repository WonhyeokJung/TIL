T = int(input())

for tc in range(1, T+1):
    # 가로 세로길이 N , 단어의 길이 K
    N, K = map(int, input().split())
    # 퍼즐 1은 빈부분, 0은 글씨 못쓰는 부분
    arr = []

    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 최종 결과를 담을 result
    result = 0
    # K 길이의 글씨 쓸수 있는 칸 세기
    count = 1
    for i in range(N):
        for j in range(0,N-1):
            if arr[i][j] == arr[i][j+1] == 1:
                count += 1
                if j == N-2:
                    if count == K:
                        result += 1
                        count = 1
                    else:
                        count = 1
            else:
                if count == K:
                    result += 1
                count = 1

    # 열에서 같은 작업 반복
    for i in range(N):
        for j in range(0,N-1):
            if arr[j][i] == arr[j+1][i] == 1:
                count += 1
                if j == N-2:
                    if count == K:
                        result += 1
                        count = 1
                    else:
                        count = 1
            else:
                if count == K:
                    result += 1

                count = 1
    print("#{} {}".format(tc, result))