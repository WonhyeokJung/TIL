# Test Case
T = int(input())

for tc in range(1, T + 1):
    # 행N과 열M
    N, M = map(int, input().split())
    # 정원 나무 담을 2차원 배열
    arr = [[] * M for i in range(N)]
    # 나무의 총 비용
    total_cost = 0
    # 심은 나무의 수
    trees = 0
    # 가장 비싼 나무의 가격
    max_cost = 0
    # 가장 비싼 나무가 심어진 열. 중복이 있으면 가장 큰 열 번호를 기준
    max_col = 0

    # 각 정원번호 2차원 배열에 담기
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # 나무 심은 곳 구하기
    # (홀수열(1,3,5...)만 나무를 심으므로, 두칸씩 이동한다.)
    for i in range(0, M, 2):
        # 열과 행의 길이도 다르고, 열은 한줄씩 건너띄지만 행은 전부 돌아야하기 때문에 range N
        for j in range(N):
            # 나무의 총 비용은 각 칸의 값을 더한 값
            total_cost += arr[j][i]
            # 심은 나무 수는 for문이 도는만큼 1씩 올려주면 완성된다.
            trees += 1
            # 가장 비싼 나무의 가격 구하기. 다만 max_cost가 같을 때도 if문이 동작하게 해주었는데... max_col때문이다.
            if arr[j][i] >= max_cost:
                # 가장 비싼 나무의 가격
                max_cost = arr[j][i]
                # 가장 비싼 나무가 심어진 열은 가장 비싼 나무의 가격이 중복되면 가장 큰 열 번호를 기준으로 하기 때문이다..
                # 그리고 i는 index이므로, 1을 더해줘서 우리가 원하는 열 번호를 출력한다.
                max_col = i + 1
    # 출력문
    print("#{} {} {} {} {}".format(tc, total_cost, trees, max_cost, max_col))
