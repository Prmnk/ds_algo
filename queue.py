class queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue==[]

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        data = self.queue[0]
        return data

    def queuesize(self):
        return len(self.queue)


queue = queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print(queue.queuesize())
print("dequeue: ", queue.dequeue())