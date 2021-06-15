class Node(object):

    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.predeccesor = None

class DepthFirstSearch(object):

    def dfs(self,startnode):
        startnode.visited = True
        print("%s "%startnode.name)

        for n in startnode.adjacency_list:
            if not n.visited:
                self.dfs(n)

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node5)

dfs = DepthFirstSearch()

dfs.dfs(node1)