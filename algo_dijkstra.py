import sys
import heapq

class Edge(object):
    def __init__(self, weight, start, target):
        self.weight = weight
        self.startVertex = start
        self.targetVertex = target

class Node(object):
    def __init__(self, name):
        self.name = name
        self.IsVisited = False
        self.predeccesor = None
        self.adjacency_list = []
        self.MinDistance = sys.maxsize
    
    def __cmp__(self, otherVertex):
        return self.cmp(self.MinDistance, otherVertex.minDistance)

    def __lt__(self,otherVertex):
        selfPriority = self.MinDistance
        otherPriority = otherVertex.MinDistance
        return selfPriority < otherPriority

class Algorithm(object):

    # can't handle negative edge weights - use bellman ford for that
    # choose edge greedly

    def calculateShortestPath(self, vertexList, startVertex):
        q = []
        startVertex.MinDistance = 0
        heapq.heappush(q,startVertex)

        while len(q)>0:
    
            actualVertex = heapq.heappop(q)

            for edge in actualVertex.adjacency_list:
                
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.MinDistance + edge.weight
                

                if newDistance < v.MinDistance:
                    v.predeccesor = u
                    v.MinDistance = newDistance
                    heapq.heappush(q,v)

    def shortestPass(self, targetVertex):
        node = targetVertex

        while node is not None:
            print(node.name)
            node = node.predeccesor


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

edge1 = Edge(5,node1, node2)
edge2 = Edge(8,node1, node8)
edge3 = Edge(9,node1, node5)
edge4 = Edge(15,node2, node4)
edge5 = Edge(12,node2, node3)
edge6 = Edge(4,node2, node8)
edge7 = Edge(7,node8, node3)
edge8 = Edge(6,node8, node6)
edge9 = Edge(5,node5, node8)
edge10 = Edge(4,node5, node6)
edge11 = Edge(20,node5, node7)
edge12 = Edge(1,node6, node3)
edge13 = Edge(13,node6, node7)
edge14 = Edge(3,node3, node4)
edge15 = Edge(11,node3, node7)
edge16 = Edge(9,node4, node7)

node1.adjacency_list.append(edge1)
node1.adjacency_list.append(edge2)
node1.adjacency_list.append(edge3)
node2.adjacency_list.append(edge4)
node2.adjacency_list.append(edge5)
node2.adjacency_list.append(edge6)
node8.adjacency_list.append(edge7)
node8.adjacency_list.append(edge8)
node5.adjacency_list.append(edge9)
node5.adjacency_list.append(edge10)
node5.adjacency_list.append(edge11)
node6.adjacency_list.append(edge12)
node6.adjacency_list.append(edge13)
node3.adjacency_list.append(edge14)
node3.adjacency_list.append(edge15)
node4.adjacency_list.append(edge16)

vertexList=(node1, node2, node3, node4, node5, node6, node7, node8)

Algo = Algorithm()
Algo.calculateShortestPath(vertexList, node1)
#print(node1.MinDistance,node2.MinDistance, node3.MinDistance, node4.MinDistance, node5.MinDistance, node6.MinDistance, node7.MinDistance, node8.MinDistance)
Algo.shortestPass(node7)



    