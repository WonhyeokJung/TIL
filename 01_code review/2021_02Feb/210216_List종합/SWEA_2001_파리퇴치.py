T = int(input())

for tc in range(1, T+1):
    # N*N배열크기, M*M 파리채크기
    N, M = map(int,input().split())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    max_killed = 0
    # i, j가 M 크기를 그릴 기준 좌표값(행과 열)
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            killed = 0
            # 각행, 각열을 M 길이만큼 돌면서 값을 다 더한다.
            for k in range(i, i+M):
                for l in range(j, j+M):
                    killed += arr[k][l]
            # 맥스값 체크.
            if killed > max_killed:
                max_killed = killed
    print("#{} {}".format(tc, max_killed))