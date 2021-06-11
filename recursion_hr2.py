# find sum of digits using recursion
n= '123'
k = 3

import functools

def superdig(n,k):
    dig = k*n

    def super_dig_rec(dig):
        if len(dig) == 1:
             return dig
        dig_sum = functools.reduce(lambda a,b : int(a)+int(b), dig)
        return super_dig_rec(str(dig_sum))

    return super_dig_rec(dig)

     
print(superdig(n,k))

# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        self.cnt = 0     
        
        def traverseinorder(node):
            
            if node.val >= low and node.val <= high:
                self.cnt += node.val
            
            if node.left is not None and node.val > low :
                traverseinorder(node.left) 
            if node.right is not None and node.val < high:
                traverseinorder(node.right)
                
        traverseinorder(root)
        
        return self.cnt



def combination_xor(arr):
    res = 0
    for i in range(1, len(arr)+1):
        for arry in itertools.combinations(arr,i):
            su = functools.reduce(lambda x,y: x^y,list(arry))
            res += su
    return res


#https://leetcode.com/problems/increasing-order-search-tree/
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.result = d =  TreeNode(0)
        
        def traverse_in_order(node):
            if node.left is not None:
                traverse_in_order(node.left)
            
            self.result.right = TreeNode(node.val)
            self.result = self.result.right
            
            if node.right is not None:
                traverse_in_order(node.right)
                
        traverse_in_order(root) 
        return d.right