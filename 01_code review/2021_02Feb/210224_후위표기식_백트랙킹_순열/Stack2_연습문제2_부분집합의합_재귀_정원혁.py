# idx개의 항을 갖는 부분집합 출력
def powerset(idx):
    if idx == N:
        ans = 0
        for i in range(N):
            if result[i]:
                ans += sets[i]
                result[i] = sets[i]
        if ans == 10:
            for i in range(len(result)):
                if result[i] != 0:
                    print(result[i], end=" ")
            print()


    else:
        for i in range(2):
            # 0 1 0 1 0 1 0 1
            result[idx] = i
            powerset(idx+1)


# powerset 중 원소의 합이 10인 부분집합 구하기
sets = [1, 2 ,3, 4, 5, 6, 7, 8 ,9, 10]
# 1, 0 결과 담을 result
result = [0]*10
N = 10
# 총 2**10개가 나올것. # Print에 조건문이 없다면
powerset(0)