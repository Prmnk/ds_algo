class Node:
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data

    
class bst(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if data < node.data:
            if node.left:
                self.insertNode(data,node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data,node.right)
            else:
                node.right = Node(data)

    def getminval(self):
        if self.root:
            return self.getmin(self.root)

    def getmin(self,node):
        if node.left:
            return self.getmin(node.left)
        return node.data

    def getmmaxval(self):
        if self.root:
            return self.getmax(self.root)

    def getmax(self,node):
        if node.right:
            return self.getmax(node.right)
        return node.data

    def traverse(self):
        if self.root:
            self.traverseinorder(self.root)

    def traverseinorder(self,node):
        if node.left:
            self.traverseinorder(node.left) # first left

        print("%s " % node.data) # then root

        if node.right:
            self.traverseinorder(node.right) # then right


bst = bst()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(11)

print(bst.getminval())

bst.traverse()

    

