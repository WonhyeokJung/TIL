# List로 구현해보기

arr = []
# 3개의 데이터 넣고, 다시 3번 꺼내 출력하기
for i in range(3):
    arr.append(i)
print(arr)
for i in range(3):
    arr.pop(-1)
print(arr)


# top을 만들어 구현해보기
class Stack:
    def __init__(self, num):
        self.arr = []
        self.max_stack_size = num

    # def top(self):
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

    def push(self, items):
        if self.max_stack_size <= len(self.arr)-1:
            return "Stack is full"
        else:
            return self.arr.append(items)


a = Stack(10)
