# 원형 큐

class Queue:
    def __init__(self, n):
        # front, rear 초기값이 0
        # queue 사이즈 n
        self.queue = [""]*n
        self.front = 0
        self.rear = 0

    # 큐 뒤쪽에 원소 삽입
    def enqueue(self, items):
        if self.isfull():
            return "Queue_Full"
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = items

    # 큐 앞쪽 원소 삭제 후 반환
    def dequeue(self):
        if self.isempty():
            return "Queue_Empty"
        else:
            self.front = (self.front + 1) % len(self.queue)
            # 굳이 지우지 않고, 위치값만 반환하여 시간복잡도를 줄일 수 있음.
            return self.queue[self.front]

    # 공백 상태의 큐를 생성
    def createqueue(self):
        self.queue = []
        self.rear = -1
        self.front = -1

    def isfull(self):
        return (self.rear + 1) % len(self.queue) == self.front

    def isempty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    # 앞쪽 원소를 삭제없이 반환
    def qpeek(self):
        if self.rear == self.front:
            return "Queue is empty"
        else:
            return self.queue[0]


q = Queue(10)
print(q.queue)
q.enqueue(1)
print(q.queue)
q.enqueue(2)
q.enqueue(3)
print(q.rear)
print(q.isempty())
print(q.dequeue())
print(q.queue)
print(q.dequeue())