class Node(object):
    def __init__(self,data):
        self.data = data
        self.height  = 0
        self.left = None
        self.right = None

class AVL(object):

    def __init__(self):
        self.root = None

    def calc_height(self,Node):
        if not Node:
            return -1
        return Node.height

    def check_balance(self,Node):
        if not Node:
            return 0
        return self.calc_height(self.left) - self.calc_height(self.right)

    def settle_violation(self,data,Node):
        balance = self.check_balance(Node)

        if balance > 1 and data < Node.left.data:
            return self.rotate_right(Node)

        if balance < -1 and data > Node.right.data:
            return self.rotate_left(Node)

    def rotate_right(self,node):
        return None
        
    def rotate_left(self,node):
        return None
