# Test Case
T = int(input())

for tc in range(1, T+1):
    # 누가 먼저인지 확인한다.
    first = input()
    # A의 주사위를 list로 받는다.
    A_arr = list(map(int, input().split()))
    # B의 주사위를 list로 받는다.
    B_arr = list(map(int, input().split()))
    # A의 현재 위치
    A_location = 0
    # B의 현재 위치
    B_location = 0
    # 승자가 누구인지 알려줄 winner 변수
    winner = ""

    # A가 먼저일 때
    if first == "A":
        # 각 주사위 카운트을 센다.
        count = 0
        while count < len(A_arr):
            # count번째 주사위만큼 A_location을 움직인다.
            A_location += A_arr[count]
            # A가 움직인 후, A_location이 B_location과 같아졌다면, B의 말의 location이 0이 되어야 한다.
            # B의 말을 A가 잡아먹었기 때문.
            if A_location == B_location:
                B_location = 0

            B_location += B_arr[count]
            # 위와 반대로 A말의 로케이션이 0이 되어야 한다.
            if A_location == B_location:
                A_location = 0

            # 승자 확인
            if A_location >= 19:
                winner = "A"
                break
            elif B_location >= 19:
                winner = "B"
                break
            # 위 과정에서 winner가 나오지 않고, count는 10이 되었다면 누구도 결과에 도달하지 못한 것이므로 무승부이다.
            elif count == 9:
                winner = "AB"
                break

            # 다음 주사위를 위해 count + 1
            count += 1

    # B가 먼저일 때
    if first == "B":
        # 각 주사위 카운트을 센다.
        count = 0
        while count < len(A_arr):
            # B_location을 먼저 이동하는 것이 A가 먼저일 때와 다른 점이다.
            B_location += B_arr[count]
            if A_location == B_location:
                A_location = 0

            # 그 다음 A 로케이션
            A_location += A_arr[count]
            if A_location == B_location:
                B_location = 0

            # 둘다 20을 넘은게 아니라면 각자 승자 확인. 위와 같음
            if B_location >= 20:
                winner = "B"
                break
            elif A_location >= 20:
                winner = "A"
                break
            elif count == 9:
                winner = "AB"
                break
            # 다음 주사위를 위해 count + 1
            count += 1
        
    print("#{} {}".format(tc, winner))