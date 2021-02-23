# 인접 List를 이용한 구현

# 두 개의 정점 사이 간선이 나열된 arr. 모든 정점을 깊이 우선 탐색하여, 화면ㅅ에 깊이 우선 탐색 경로를 출력

arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# 1은 2와 3과 연결, 2는 4와 5와 연결(1과 연결된건 앞에서 나왔으므로 생략됨

visited = ["F"]*7
adjacency = [[] for _ in range(7)]
stack = []

# 각 2차원배열에 연결된 노드 번호 넣기
for i in range(0, len(arr), 2):
    adjacency[arr[i]-1].append(arr[i+1])
    adjacency[arr[i+1]-1].append(arr[i])

#출력 참고
print(adjacency)
# 1번부터 탐색 시작
visited[0] = "T"
# 현재 위치 저장
n = 1
# 결과값을 젖아할 list
result = [n]
# 방문하지 않은 곳이 있다면 계속 돌면서
while "F" in visited:
    # stack에 내 출발지점을 넣는다.
    if not n in stack:
        stack.append(n)
    # 현재 위치에서 갈 수 있는 노드 번호들을 탐색
    for i in range(len(adjacency[n-1])):
        # 연결된 노드의 visited 값이 F라면
        if visited[adjacency[n-1][i]-1] == "F":
            # 그 노드 번호가 새로운 n이 되고
            n = adjacency[n-1][i]
            # 그 노드는 방문한 곳이 된다
            visited[n-1] = "T"
            # 탈출
            break
    # 방문하지 않은 인접 노드가 없다면 스택 한칸 전으로 돌아가서 다시 수행한다.
    else:
        stack.pop(-1)
        n = stack[len(stack)-1]
    # 결과값 저장(경로저장)
    if not n in result:
        result.append(n)
    print(stack)
print(*result)


