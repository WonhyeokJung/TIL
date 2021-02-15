# 각 부분집합의 합 중 합이 10이 되는 부분 집합의 출력

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
# 결과를 한번에 담을 List
result = []
for i in range(1<<n):  # 1을 n만큼 왼쪽으로. 즉, 전체 부분집합의 총 개수
    #집합 리스트
    ans = []
    # 합이 10인가 확인하기 위한 임시 변수
    sum_10 = 0
    for j in range(n):
        if i & (1 << j): # 컴퓨터는 2진수로 봄
            sum_10 += arr[j]
            # for j문이 돌면서 ans에 계속 값을 새로 만드는게 아닌, 값을 추가함. 그래서 여러 집합이 나올 수 있음.
            ans += [arr[j]]
            # 무엇이 나오는지 연습 검증
            print(i,j,ans) 
    if sum_10 == 10:
        result.append(ans)
print(result)
