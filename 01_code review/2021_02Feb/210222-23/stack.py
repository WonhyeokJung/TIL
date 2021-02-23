class Stack:
    # 리스트를 이용하여 스택 생성
    def __init__(self):
        self.top = []

    # 스택의 크기를 출력
    def __len__(self):
        return len(self.top)

    # 스택 내부 자료를 string으로 변환하여 반환
    def __str__(self):
        return str(self.top[::1])

    # 스택 초기화
    def clear(self):
        self.top = []

    # PUSH
    def push(self, item):
        self.top.append(item)

    # POP
    def pop(self):
        # if Stack is not empty
        if not self.isEmpty():
            # pop and return
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()

    # 자료가 포함되어 있는지 여부 반환
    def isContain(self, item):
        return item in self.top

    # 스택에서 top의 값을 읽어온다
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()

    # 스택이 비어있는지 확인
    def isEmpty(self):
        return len(self.top) == 0

    # 스택 크기 반환
    def size(self):
        return len(self.top)

    # iterator를 이용하여 스택 출력
    def __iter__(self):
        return _StackIterator(self.top)


# Iterator
class _StackIterator:
    def __init__(self, theList):
        self._items = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._items):
            item = self._items[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration

a = Stack()
print(a.__len__())