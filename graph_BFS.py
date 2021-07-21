class Node(object):

    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.predeccesor = None

class BreadFirstSearch(object):

    def bfs(self, startnode):
        queue =  []
        queue.append(startnode)
        startnode.visited = True

        while queue:
            actualnode = queue.pop()
            print("%s " %actualnode.name)

            for n in actualnode.adjacency_list:
                if not n.visited:
                    queue.append(n)
                    n.visited = True

def levelOrder(self, root: 'Node') :
    if root is None:
        return []
    res= []
    queue = [root]
    new_q = []
    
    while queue:
        tmp=[]            
        for n in queue:
            tmp.append(n.val)
            if n.children is not None:
                new_q += n.children
                
        res.append(tmp)
        queue = new_q
        new_q = []
    
    return res
        

                
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node5)

bfs = BreadFirstSearch()

bfs.bfs(node1)

        