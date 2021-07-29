class Node:
    def __init__(self,key) :
        self.left = None
        self.right = None
        self.data = key

# level order traversal

def hieght(node):
    if node is None:
        return 0
    else:
        lht = hieght(node.left)
        rht = hieght(node.right)

        if lht>rht:
            return lht+1
        else:
            return rht+1


def printlevelorder(root):
    h = hieght(root)
    for i in range(1,h+1):
        printcurrentlevel(root,i)

def printcurrentlevel(root,level):
    if root is None: #exit condition 1
        return 
    if level==1: #exit condition 2
        print(root.data, end = " ")
    else:
        printcurrentlevel(root.left, level-1)
        printcurrentlevel(root.right,level-1)



    



    
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)

print(hieght(root))
print(printlevelorder(root))

