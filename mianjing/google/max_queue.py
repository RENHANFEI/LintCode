class MaxQueue(object):

    def __init__(self):
        self.queue = []
        self.max_queue = []

    def enqueue(self, num):
        self.queue.append(num)
        while self.max_queue and self.max_queue[-1] < num:
            self.max_queue.pop()
        self.max_queue.append(num)

    def dequeue(self):
        num = self.queue[0]
        self.queue.pop(0)
        if self.max_queue[0] == num:
            self.max_queue.pop(0)
        return num

    def get_max(self):
        return self.max_queue[0]

q = MaxQueue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
print(q.get_max())
print(q.dequeue())
print(q.dequeue())
print(q.get_max())
q.enqueue(4)
print(q.get_max())