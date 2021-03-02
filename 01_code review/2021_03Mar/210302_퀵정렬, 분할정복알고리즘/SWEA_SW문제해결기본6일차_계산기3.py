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
            return self.stack[len(self.stack) - 1]
        else:
            return -1

    def top(self):
        return self.top()


T = 10
for tc in range(1, T + 1):
    N = int(input())
    m = list(input())
    # 연산자 담을 스택
    s = Stack()
    # 결과담을 것
    result = []
    token = ["(", "*", "/", "+", "-", ")"]

    # 밖에서 처음 들어갈 때, 우선순위 0: ( 1: *, /  2: +, - # 사칙연산은 동순위 만나면 그 친구를 뺴주고 본인이 들어가야함. 따라서 왼 괄호는 무조건 들어간다.
    # 안에서 나와야 하는 우선순위 1: *, / 2: +,- 3: ( // 동순위 만나면 괄호는 그대로, 사칙연산은 나와야만 한다.
    # 안에서 (는 )만이 빼줄 수 있다.

    for i in range(len(m)):
        # 숫자면 일단 result에 그냥 넣기
        if not m[i] in token:
            result.append(m[i])
        # 아니라면
        else:
            if m[i] == "(":  # 왼괄호는 그냥 들어감. 들어갈땐 1순위
                s.push(m[i])
            elif m[i] == "*" or m[i] == "/":
                # 스택 길이만큼 찾아보면서
                for j in range(len(s.stack)):
                    # 내가 처음이거나, ( + - 라면 그냥 들어간다. for문 종료 위한 break
                    if s.top == -1 or s.peek() == token[0] or s.peek() == token[3] or s.peek() == token[4]:
                        # for문을 종료하자
                        break
                    else:  # * / 일 경우는 s.pop()을 result에 넣고, 계속 순환.
                        result.append(s.pop())
                # 현재 것 넣어주기
                s.push(m[i])
            elif m[i] == "+" or m[i] == "-":
                for k in range(len(s.stack)):
                    # 내가 처음이거나, "("가 peek라면 역시 그냥 들어간다.
                    if s.top == -1 or s.peek() == token[0]:
                        break
                    else:
                        result.append(s.pop())
                # 입장
                s.push(m[i])
            else:  # )
                for l in range(len(s.stack)):
                    if s.peek() != token[0]:
                        result.append(s.pop())
                    else:  # ( 만나면
                        s.pop()
                        break

    # for문을 다 돌고, ()를 사용하지 않고 연산한 경우에는, Stack에 미처 나오지 못한 사칙연산이 있을 수 있음.
    if s.stack:  # 스택이 아직 남아있다면,
        # 돌면서 result에 붙이기
        while s.stack:
            result.append(s.pop())

    # 이제 나온 result 계산
    # 최종 연산 결과를 담을 스택엔 피연산자만 들어간다.
    s2 = Stack()
    # 위에서 구한 후위표기식의 결과를 돌면서
    for i in range(len(result)):
        # 피연산자는 그냥 넣고
        if not result[i] in token:
            s2.push(result[i])
        # 연산자라면 피연산자 2개를 꺼내와서, 연산자가 무엇인지 for문을 돌며 찾아서
        # 그 연산자로 계산을 실행하고, 다시 그 결과값을 stack에 push한다.
        else:
            b = int(s2.pop())
            a = int(s2.pop())
            # eval()을 쓰면 이 과정은 필요없긴 하다. 어찌됐건,
            # 계산 후 계산결과를 다시 stack에 push()한다. 연산을 지속하기 때문
            for k in token:
                if token[1] == result[i]:
                    s2.push(a * b)
                    break
                if token[2] == result[i]:
                    s2.push(a / b)
                    break
                if token[3] == result[i]:
                    s2.push(a + b)
                    break
                if token[4] == result[i]:
                    s2.push(a - b)
                    break
        # eval 사용시 if문 필요없음

    print("#{} {}".format(tc, s2.stack[0]))