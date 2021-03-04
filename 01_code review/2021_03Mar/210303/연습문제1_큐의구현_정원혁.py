# 선형 큐

class Queue:
    def __init__(self, n):
        self.queue = []
        self.front = -1
        self.rear = -1
        # n = 큐 길이
    # 큐 뒤쪽에 원소 삽입
    def enqueue(self, n):
        if self.isfull():
            return "Queue_Full"
        else:
            self.rear += 1
            return self.queue.append(n)
    
    # 큐 앞쪽 원소 삭제 후 반환
    def dequeue(self):
        if self.rear == self.front:
            return "underflow"
        else:
            self.front += 1
            return self.queue.pop(0)
    
    # 공백 상태의 큐를 생성
    def createqueue(self):
        self.queue = []
        self.rear = -1
        self.front = -1
    
    def isfull(self):
        return self.rear == self.n-1

    def isempty(self):
        if self.rear == self.front:
            return True
        else:
            return -1

    # 앞쪽 원소를 삭제없이 반환
    def qpeek(self):
        if self.rear == self.front:
            return "Queue is empty"
        else:
            return self.queue[0]


# 3개의 데이터 123 삽입후, 세개의 데이터를 차례로 꺼내서 출력
q = Queue(10)
q.enqueue(1)
print(q.queue)
q.enqueue(2)
print(q.queue)
q.enqueue(3)
print(q.queue)
# 데이터 꺼내기
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.front, q.rear)