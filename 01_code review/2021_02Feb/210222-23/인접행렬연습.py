# 인접행렬 만들어보기
"""
7 8 정점수, 간선수
1 2 이어지는 두 정점
1 3
2 4
2 5
4 6
5 6
6 7
3 7
"""

V, E = map(int,input().split())
arr = [[0]*V for _ in range(V)]

for i in range(E):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1
    arr[x-1][y-1] = 1

for i in arr:
    print(*i)