# 재귀 이용해 풀어보기
def reculsive_dfs(graph, n):
    visit = list()
    stack = list()

    stack.append(n)

    while stack:
        node = stack.pop(-1)
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


