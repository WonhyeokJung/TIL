T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    # 버블 정렬 오름차순.
    for j in range(N-1,0,-1):
        for k in range(0,j):
            if N_list[k] > N_list[k+1]:
                N_list[k], N_list[k+1] = N_list[k+1], N_list[k]

    print("#{}".format(tc), end=" ")
    # 배열의 원소를 하나로 이어붙여주는 join 메서드
    print(" ".join(map(str, N_list)))
