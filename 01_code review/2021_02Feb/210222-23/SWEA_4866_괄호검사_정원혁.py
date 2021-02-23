# Stack 예제
class Stack():
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
    text = input()
    stack = []
    result = 0
    for i in text:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if not stack:
                stack.append(")")
                break
            if stack[len(stack) - 1] != "(":
                break
            else:
                stack.pop()

        if i == "{":
            stack.append("{")
        elif i == "}":
            if not stack:
                stack.append("}")
                break
            if stack[len(stack) - 1] != "{":
                break
            else:
                stack.pop()

    if not stack:
        result = 1

    print("#{} {}".format(tc, result))
