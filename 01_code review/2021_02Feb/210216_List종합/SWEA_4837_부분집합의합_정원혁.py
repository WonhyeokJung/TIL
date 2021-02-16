# Test Case
T = int(input())

# 테스트 케이스만큼 돌면서

for tc in range(1, T+1):
    # 1~12까지를 원소로 갖는 집합 A, A중 N개의 원소를 갖는 A의 부분집합, N의 원소의 합 K
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    N, K = map(int, input().split())

    # 각 원소의 합이 K인 부분집합의 개수
    result = 0

    # 전체 부분집합 개수
    for i in range(1<<12):
        # 각 부분 집합 ans 초기화
        ans = []
        
        # 전체 원소수랑 비교하여 부분집합 구하기
        for j in range(12):
            if i & (1 << j):
                ans.append(A[j])

        # 임의로 만든 ans 길이가 N과 같다면
        if len(ans) == N:
            # 원소의 합 변수 sums
            sums = 0

            # 부분집합의 원소 k 다 더하고
            for k in ans:
                sums += k
            # 그 합 sums가 우리가 input한 K와 같다면
            if sums == K:
                result += 1


    # 출력문
    print("#{} {}".format(tc, result))