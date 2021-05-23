class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node = None

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

    def list_length(self):
        if self.head is None:
            return 0
        current = self.head 
        len = 0

        while (current is not None):
            len += 1
            current = current.next_node
        return len

    def search_data(self,search_data):
        current = self.head
        pos = 0

        while current is not None:
            pos +=1
            if current.data == search_data:
                return pos
            current = current.next_node
                 
        if current is None:
            return -1
                

    def insert_at_begin(self,new_data):
        new_node = Node(new_data)
        self.size += 1

        if self.head is None:
            self.head = new_node
            return

        new_node.next_node = self.head
        self.head = new_node

    def insert_after(self,prev_node,new_data):
        new_node = Node(new_data)
        new_node.next_node = prev_node.next_node 
        prev_node.next_node = new_node
        self.size += 1

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        self.size += 1
        
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next_node):
            last = last.next_node

        last.next_node = new_node

    def delete_node_data(self,key_data):
        current = self.head
        
        if current.data == key_data:
            self.head = None
            return
        prev = self.head
        while (current is not None):
            if current.data == key_data:
                break
            prev = current
            current = current.next_node
        
        prev.next_node = current.next_node
        current = None

    def delete_node_pos(self,position):
        current = self.head 
        prev = self.head
        pos = 1

        if position == 1:
            self.head = None
            return

        while (current is not None):
            
            if pos == position:
                break
            prev = current
            current = current.next_node
            pos += 1
        
        prev.next_node = current.next_node
        current = None

    def delete_full_list(self):
        current = self.head

        while current is not None:
            next = current.next_node
            del current.data
            current = next

        self.head = None



    def reverse_ll(self):
        prev = None
        current = self.head
        
        if current.next_node == None or current is None: # check if there is less than 2 nodes in the linked list
            return current

        while(current is not None):
            next = current.next_node # save for later operations
            current.next_node = prev # swap pointer for next node of current node
            prev = current #change for next loop
            current = next #change for next loop
        self.head = prev # update head of the linked list

    def reverse_ll_recursive(self,prev = None):
        self.print_list()
        current = self.head
        next = current.next_node
        
        current.next_node = prev
        prev = current
        self.head = next
        if next == None or current is None:
            return current
        self.reverse_ll_recursive(prev)




if __name__ == '__main__':
    l_lst = linked_list()
    
    l_lst.head= Node(1)
    second = Node(2)
    third = Node(3)

    l_lst.head.next_node= second
    second.next_node = third

    l_lst.insert_at_begin(0)
    l_lst.insert_after(l_lst.head.next_node,1.5)
    l_lst.insert_at_end(4)
    print('a')
    l_lst.print_list()
    l_lst.delete_node_data(3)
    #l_lst.reverse_ll()
    #l_lst.reverse_ll_recursive(None)
    l_lst.print_list()
    l_lst.delete_node_pos(2)
    l_lst.print_list()
    print(l_lst.list_length())
    print(l_lst.search_data(6))
    l_lst.delete_full_list()
    l_lst.print_list()
    print(l_lst.list_length())



