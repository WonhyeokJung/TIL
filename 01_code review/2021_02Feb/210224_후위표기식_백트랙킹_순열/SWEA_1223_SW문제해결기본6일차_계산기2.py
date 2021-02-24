class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, n):
        self.top += 1
        return self.stack.append(n)

    def pop(self):
        if self.top > -1:
            self.top -= 1
            return self.stack.pop()
        else:
            return "underflow"

    def peek(self):
        if self.top > -1:
            return self.stack[len(self.stack)-1]
        else:
            return -1

    def top(self):
        return self.top()



T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    s = Stack()
    # 괄호까지 넣은 결과값
    current = 0
    i = 0
    while i < N-2:  # == len(cal)
        if arr[i] == "*":
            current = int(s.pop()) * int(arr[i+1])
            if not arr[i+2] == "*":  # 뒤에가 곱연산이 아니면 앞에꺼 다 꺼내와서 더하기
                j = len(s.stack)
                while j > 0 :
                    s.pop() # 덧셈기호 제거
                    j -= 1
                    current += int(s.pop())  # 현재 연산 끝난값
                    j -= 1
                s.push(current)  # 다시 넣어주기
            else:  # 뒤에가 곱연산이면 지금 숫자 넣고 그냥 진행
                s.push(current)
            i += 2  # 곱연산을 해버렸으니 i 한번 더 더해주기
        else:  # 현재 곱연산도 아니고, 마지막 항도 아니라면 그냥 계속 스택 푸쉬
            s.push(arr[i])
            i += 1
    # N-2(기호) ~ N-1(숫자) & 남은 스택 처리
    result = 0
    if arr[N-2] == "*":
        result += int(arr[N-1]) * int(s.pop())
        if s.stack:  # 스택 여전히 차있으면
            j = len(s.stack)
            while j > 0:
                s.pop()  # 덧셈기호 제거
                j -= 1
                result += int(s.pop())  # 숫자 더하기
                j -= 1
    else:  # 덧셈
        result += int(arr[N - 1]) + int(s.pop())
        if s.stack:  # 스택 여전히 차있으면
            j = len(s.stack)
            while j > 0:
                s.pop()  # 덧셈기호 제거
                j -= 1
                result += int(s.pop())  # 숫자 더하기
                j -= 1

    print("#{} {}".format(tc, result))

