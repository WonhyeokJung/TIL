# LinkedListQueue

# 노드 생성
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.queue = []
        self.front = None
        self.rear = None
        # n = 큐 길이

    # 큐 뒤쪽에 원소 삽입
    def enqueue(self, item):
        if self.isempty():
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
        return self.rear == self.n - 1

    # 공백상태 : front = rear = Null
    def isempty(self):
        return self.front == None

    # 앞쪽 원소를 삭제없이 반환
    def qpeek(self):
        if self.rear == self.front:
            return "Queue is empty"
        else:
            return self.queue[0]