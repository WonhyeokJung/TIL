T =int(input())

for t in range(1, T+1):
    # 정수의 개수 n, m개씩 더한 값의 기준 m
    n, m= map(int, input().split())
    # 정수 담은 리스트
    ai = list(map(int, input().split()))

    num = 0
    # m개씩 더한 값 담을 리스트
    imsi_num_list = []
    # 리스트에 m개씩 더한 값 넣기
    for i in range(len(ai)-m+1):
        imsi_num = 0
        for j in range(m):
            imsi_num += ai[i]
            i += 1
        imsi_num_list.append(imsi_num)
    #임시 리스트 오름차순으로 정렬
    for k in range(len(imsi_num_list),0,-1):
        for l in range(0, k-1):
            if imsi_num_list[l] > imsi_num_list[l+1]:
                imsi_num_list[l], imsi_num_list[l + 1] = imsi_num_list[l+1], imsi_num_list[l]
    # 최대값과 최소값 마이너스
    num = imsi_num_list[len(imsi_num_list)-1] - imsi_num_list[0]

    print("#{} {}".format(t, num))

