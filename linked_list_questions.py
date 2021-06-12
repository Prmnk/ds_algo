
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    def reverse(self, head, k):
       
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
 
        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
 
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        print(head.data, count)
        if next is not None:
            head.next = self.reverse(next, k)
 
        # prev is new head of the input list
        return prev
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
 
 
# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
 
print ("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
 
print ("\nReversed Linked list")
llist.printList()

#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
#Definition for singly-linked list.
# merge 2 sorted linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        res_1 = ListNode(0)  
        res = res_1
        
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        while True:
            
            while l1 and (l2 is None or l1.val <= l2.val) :
                res.next = ListNode(l1.val)
                l1 = l1.next
                res = res.next
                #print (res)
                
            while l2 and ( l1 is None or l2.val <= l1.val)  :
                res.next = ListNode(l2.val)
                l2 = l2.next
                res = res.next
                #print (res)
            
            if l1 is None and l2 is None:
                break
                        
                        
        return res_1.next


