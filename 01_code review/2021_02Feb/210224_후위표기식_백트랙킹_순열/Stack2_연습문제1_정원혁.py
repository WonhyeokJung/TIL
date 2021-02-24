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


s = Stack()
m = "(2+((3*4)/5))"
result = []
token = ["(", "*", "/", "+", "-", ")"]

for i in range(len(m)):
    # 숫자면 그냥 넣기
    if not m[i] in token:
        result.append(m[i])
    # 아니라면
    else:
        if m[i] == "(":  # 왼괄호는 그냥 들어감.
            s.push(m[i])
        elif m[i] == "*" or m[i] == "/":
            for j in range(len(s.stack)):
                # ( + - 라면 그냥 들어간다
                if s.top == -1 or s.peek() == token[0] or s.peek() == token[3] or s.peek() == token[4]:
                    break
                elif s.peek() == token[1] or s.peek() == token[2]:
                    result.append(s.pop())
            s.push(m[i])
        elif m[i] == "+" or m[i] == "-":
            for k in range(len(s.stack)):
                if s.peek() == token[1] or s.peek() == token[2] or s.peek() == token[3] or s.peek() == token[4]:
                    result.append(s.pop())
                elif s.top == -1 or s.peek() == token[0]:
                    break
            s.push(m[i])
        else:  # )
            for l in range(len(s.stack)):
                if s.peek() != token[0]:
                    result.append(s.pop())
                else:  # ( 만나면
                    s.pop()
                    break


print(result)


# 이제 나온 result 계산
# 스택엔 피연산자가 들어간다.
s2 = Stack()
stack = []
for i in range(len(result)):
    if not result[i] in token:
        s2.push(result[i])
    else:
        b = int(s2.pop())
        a = int(s2.pop())
        for k in token:
            if token[1] == result[i]:
                s2.push(a*b)
                break
            if token[2] == result[i]:
                s2.push(a/b)
                break
            if token[3] == result[i]:
                s2.push(a+b)
                break
            if token[4] == result[i]:
                s2.push(a-b)
                break
    # eval 사용시 if문 필요없음

if len(s2.stack) == 1:
    print(s2.pop())
    print(s2.stack)