# 0번에서 99번에 갈 수 있는 지 구현합니다.

def dfs(n):
    visited[n] = True
    # 해당 Node에서 갈 수 있는 Node 돌며 방문 검사
    for i in arr[n]:
        if not visited[i]:
            dfs(i)

for T in range(1, 11):
    # Test Case 번호와 간선수
    tc, R = map(int, input().split())
    num_arr = list(map(int, input().split()))  # 간선 입력받기
    arr = [[] for _ in range(100)] # 인접 List
    visited = [False]*100

    # 간선 입력 한번에 받았으므로, 2개씩 잘라주며 arr[앞번호](출발Node)에 [다음번호](도착Node) append
    for i in range(0, len(num_arr), 2):
        arr[num_arr[i]].append(num_arr[i+1])

    dfs(0)
    # 99번항에 도착했나요?
    if visited[99]:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))
