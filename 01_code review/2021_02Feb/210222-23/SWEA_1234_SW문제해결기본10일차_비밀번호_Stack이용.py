# 돌면서 붙은 숫자 제거하기
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

# Test Case
T = 10

for tc in range(1, T+1):
    # 문자열 길이와 그 문자
    N, text = input().split()
    N = int(N)
    text = list(text)
    
    # 스택 실행
    result = Stack()

    # text 길이만큼 돌면서
    for i in range(len(text)):
        # text stack에 넣고
        result.push(text[i])
        # 스택 index가 1이상일때
        if result.top() >= 1:
            # Stack 서로 같으면 두값을 stack에서 빼기. text길이만큼 반복
            if result.stack[result.top()] == result.stack[result.top()-1]:
                result.pop()
                result.pop()

    print(''.join(result.stack))

