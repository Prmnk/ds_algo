class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self):
        temp = self.head
        linked_lst_string = ''
        if self.head is None:
            print ('Nothing')
            return
        
        while (temp):
            linked_lst_string =  (linked_lst_string + str(temp.data) + ' -> ')
            temp=temp.next_node
        print( linked_lst_string)
