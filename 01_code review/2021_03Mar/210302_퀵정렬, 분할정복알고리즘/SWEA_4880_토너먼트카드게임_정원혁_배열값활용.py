# 가위바위보 게임
# 분할 정복 알고리즘 활용 문제
# 1은 가위, 2는 바위, 3은 보

# 출력을 인덱스 번호+1로 해야해서 각 인덱스 번호 기준으로 구한다.
def dnc(arr):
    le = len(arr)
    # 자를게 없으면 나 혼자라는 뜻. 자신을 return시킨다
    if le == 1:
        return arr[0]

    # 하나씩 하나씩 전부 부분으로 나누기. 하다보면 다 나뉨
    # 그룹1에서 또 그룹 1 2로 나뉘고 하기 때문에, 결국엔 12 34 이런 식으로 붙을 수 있다.
    group_1 = dnc(arr[:le//2])
    group_2 = dnc(arr[le//2:])

    # 무승부
    if group_1 == group_2:
        return group_1

    elif (group_1 == 1 and group_2 == 3 or
          group_1 == 2 and group_2 == 1 or
          group_1 == 3 and group_2 == 2):
        return group_1
    else:
        return group_2


T = int(input())

for tc in range(1, T+1):
    # 인원수 N
    N = int(input())

    # 각 인원이 든 카드 리스트
    cards = list(map(int, input().split()))

    print(dnc(cards))

###########
# input 예
'''
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

Output
2 (3번쨰)
3 (5번쨰)
1 (첫번째)
'''