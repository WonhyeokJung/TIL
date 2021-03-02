# Stack 예제
class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    # 스택의 필수요소, push / top / pop / peek / isEmpty
    def push(self, items):
        return self.stack.append(items)

    def isEmpty(self):
        if self.stack:
            return False
        return True

    def peek(self):
        return self.stack[len(self.stack) - 1]  # 자료를 꺼내진 않고, 그 값만 보여주기

    def pop(self):
        if self.stack:
            return self.stack.pop()  # 맨 뒤에 것을 지우고 반환하는 pop 메서드
        return "underflow"

    def top(self):
        return len(self.stack) - 1  # top(최고항) index값 반환


T = int(input())
for tc in range(1, T + 1):
    arr = list(input().split())
    result = 0
    stack = Stack()
    operator = ["+", "-", "*", "/"]

    try:
        for i in arr:
            if i == ".":  # .은 스택에서 숫자를 꺼내 출력한다.
                result = stack.pop()
                if len(stack) != 0:
                    result = "error"
            elif i == operator[0]:
                stack.push(stack.pop() + stack.pop())
            elif i == operator[1]:
                stack.push(-stack.pop() + stack.pop())
            elif i == operator[2]:
                stack.push(stack.pop() * stack.pop())
            elif i == operator[3]:
                stack.push(int((1/stack.pop()) * stack.pop()))
            else:  # 숫자면 스택에 넣는다.
                stack.push(int(i))
    except:
        result = "error"
    print("#{} {}".format(tc, result))
