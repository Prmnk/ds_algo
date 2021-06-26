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

        print("%s " % node.data) # print node data

        if node.right:
            self.traverseinorder(node.right) # then right

    def removeNode(self,data,node):
        if not node:
            return node

        if data < node.data:
            node.left = self.removeNode(data, node.left)
        elif data > node.data:
            node.right = self.removeNode(data, node.right)
        else:
            if not node.left and not node.right:
                del node
                return None
            if not node.left:
                tmpNode = node.right
                del node
                return tmpNode
            if not node.right:
                tmpNode = node.left
                del node
                return tmpNode
            tmpnode = self.left_tree_max(node.left)
            node.data = tmpnode.data
            node.left = self.removeNode(tmpnode.data, node.left)
        return node


    def left_tree_max(self,node):
        if node.right:
             return self.left_tree_max(node.right)       
        return node

    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data, self.root)

def hasPathSum(self, root, targetSum):
    
    self.sum = 0
    
    def traverse(node, curr_sum):
        
        if not node:
            return
     
        curr_sum += node.val
        
        if node.left is None and node.right is None :
            if curr_sum == targetSum:
                return True
            else:
                return False
            
        
        return traverse(node.left, curr_sum) or traverse(node.right,curr_sum)
        
    
    return traverse(root,0)
   


bst = bst()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(11)
bst.insert(4)
bst.insert(1)

print(bst.getminval())

bst.traverse()

bst.remove(5)
bst.traverse()

    

