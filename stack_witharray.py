class stack:
    def __init__(self):
        self.stack = []  # using array/list

    def isEmpty(self):
        return self.stack == []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1] #return last item
        del self.stack[-1]
        return data
    
    def peek(self):
        data = self.stack[-1]
        return data
        
    def sizeStack(self):
        return len(self.stack)


stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.sizeStack())
print("popped :", stack.pop())
print("popped :", stack.pop())
print("peek :" , stack.peek())

