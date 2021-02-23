# List로 구현해보기

arr = []
# 3개의 데이터 넣고, 다시 3번 꺼내 출력하기
for i in range(3):
    arr.append(i)
print(arr)
for i in range(3):
    arr.pop(-1)
print(arr)

print("##############")

# 최고 크기를 조절하는 함수를 이용한 Stack
class Stack:
    def __init__(self, num):
        self.arr = []
        self.max_stack_size = num

    def top(self):
        if self.arr:
            return len(self.arr)-1

    def size(self, n):
        self.max_stack_size = n

    def isEmpty(self):
        if self.arr:
            return False
        else:
            return True

    def pop(self):
        if self.arr:
            return self.arr.pop(-1)
        else:
            print("underflow")

    def peek(self):
        return self.arr[len(self.arr)-1]

    def push(self, items):
        if self.max_stack_size <= len(self.arr):
            return "Stack is full"
        else:
            return self.arr.append(items)


a = Stack(10)
print(a.top())
a.push(1)
a.push(5)
print(a.isEmpty())
print(a.peek())
