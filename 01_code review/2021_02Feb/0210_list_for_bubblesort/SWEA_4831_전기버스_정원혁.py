# 노선수
T = int(input())

for tc in range(1, T + 1):
    # 최대 이동 가능 정류장 수 K, N번 정류장까지 가며, 충전기가 설치된 정류장 수 M
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장 M_number
    bus_stop_num = list(map(int, input().split()))
    bus_stop_num.append(N)
    # 임의의 현재 버스 위치
    bus_stop_now = 0
    # 총 충전 횟수
    result = 0
    # 남은 연료
    fuel = K

    # 최종 목적지보다 현재 정류장 값이 작을 떄
    while bus_stop_now < N:
        # 현재부터 기름으로 갈수 있는 거리가 최종 정류장 번호와 같거나 크다면
        if bus_stop_now + fuel >= N:
            break
        # 아니라면, 현재 정류장 + 연료량 더한게 충전소 정류장 번호 안에 있다면
        # 이것만 빨리 썼어도 금세 해결했는데.. 여기서 많이 시간을 소비했다.
        elif bus_stop_now + fuel in bus_stop_num:
            # 충전 1회하고
            result += 1
            # 사용한 연료만큼 더 하고
            bus_stop_now += fuel
            # 다시 연료 충전
            fuel = K
        else:
            # 연료 1회 빼고 다시 순환
            fuel -= 1
            # 이동 불가
            if fuel == 0:
                result = 0
                break


    print("#{} {}".format(tc, result))
