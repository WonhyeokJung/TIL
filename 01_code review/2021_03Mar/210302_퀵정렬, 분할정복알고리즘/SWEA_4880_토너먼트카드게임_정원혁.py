# 가위바위보 게임
# 분할 정복 알고리즘 활용 문제
# 1은 가위, 2는 바위, 3은 보

# 출력을 인덱스 번호+1로 해야해서 각 인덱스 번호 기준으로 구한다.
def dnc(start, end):
    global cards
    # 자를게 없으면 나 혼자라는 뜻. 자신을 return시킨다
    if start == end:
        # group_1 혹은 group_2에 return 이 값을 return 한다.
        return start

    # 하나씩 하나씩 전부 부분으로 나누기. 하다보면 다 나뉨
    # 그룹1에서 또 그룹 1 2로 나뉘고 하기 때문에, 결국엔 12 34 이런 식으로 붙을 수 있다.
    # 매번 새로워지는 array의 length를 start+end로 표현
    group_1 = dnc(start, (start+end)//2)
    group_2 = dnc((start+end)//2+1, end)

    # 무승부라면 빠른쪽 인덱스를 돌려준다.
    if cards[group_1] == cards[group_2]:
        return group_1

    # group_1  승리
    elif cards[group_1] == 1 and cards[group_2] == 3 or cards[group_1] == 2 and cards[group_2] == 1 or cards[group_1] == 3 and cards[group_2] == 2:
        return group_1
    else:
        return group_2


T = int(input())

for tc in range(1, T+1):
    # 인원수 N
    N = int(input())

    # 각 인원이 든 카드 리스트
    cards = list(map(int, input().split()))

    # 첫 인덱스는 0 끝 인덱스는 N-1이니까. 문제에서 첫 인덱스를 1로 읽어서, 마지막에 1을 더해줌
    print("#{} {}".format(tc, dnc(0, N-1) + 1))

