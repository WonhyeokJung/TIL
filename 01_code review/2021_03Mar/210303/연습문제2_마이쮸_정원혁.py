N = 20  # 사탕 개수
# (0,0) [0] 사람번호, [1] 마지막으로 받은 사탕 개수
queue = [(1,0)]
new_person = 1
# 마지막으로 사탕 받은 사람
last_person = 0

while N > 0:
    num, cnt = queue.pop(0)  # 받으러온 사람, 저번까지 받은 개수
    
    last_person = num
    cnt += 1  # 저번보다는 하나 더 챙기기

    N -= cnt  # 챙긴만큼 N에서 값을 빼주기
    new_person += 1

    queue.append((num, cnt))
    queue.append((new_person, 0))

    print(queue)
    print("큐에있는사람수:", len(queue))  # 큐에 있는 사람 수
    print("현재까지 나눠준 사탕수:", 20-N)
    for i in range(len(queue)):
        if queue[i][1] >= 1:
            print("현재 일인당 나눠주는 사탕수:", queue[i][0],"번 사람", queue[i][1], "개")
    print()


