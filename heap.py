class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.head = [0] * HEAP_SIZE
        self.currentPosition = -1

    def insert(self,item):
        if self.isFull():
            print("heap is full")
            return

        self.currentPosition = self.currentPosition + 1
        self.heap[self.currentPosition] = item
        self.currentPosition
        self.fixUp(self.currentPosition)

    def fixUp(self,index):
        parentIndex = int((index-1)/2)

        while parentIndex >=0 and self.heap[parentIndex] < self.head[index]:
            tmp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = tmp
            parentIndex = int((index-1)/2)

    def isFull(self):
        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False

# for max heap

    def heapsort(self):

        for i in range(self.currentPosition+1):
            tmp = self.heap[0]
            self.heap[0] = self.heap[self.currentPosition -i]
            self.heap[self.currentPosition-i] = tmp
            self.fixDown(0, self.currentPosition -i -1)

    def fixDown(self, index , upto):
        while index <= upto:
            left = 2*index + 1
            right = 2*index + 1

            if left < upto:
                childtoSwap = None
                if right > upto:
                    childtoSwap = left
                else:
                    if self.heap[left]> self.heap[right]:
                        childtoSwap = left
                    else:
                        childtoSwap = right
                if self.heap[index] < self.heap[childtoSwap]:
                    tmp = self.heap[index]
                    self.heap[index] = self.heap[childtoSwap]
                    self.heap[childtoSwap] = tmp
                else:
                    break
            else:
                break
    


