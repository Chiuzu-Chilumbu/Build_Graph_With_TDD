"""In this module we will implement our graph representation using an adjacency list"""
from collections import defaultdict

from collections import defaultdict
from app.models.queue_adt import Queue
from app.models.stack_adt import Stack

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def add_vertex(self, value):
        """Add a vertex to the graph"""
        if value not in self.adjList:
            self.adjList[value] = []

    def add_edge(self, v1, v2):
        """Add an undirected edge between two vertices"""
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)


    def bfs(self, start, queue_capacity=10):
        """Breadth-First Search using the Queue ADT"""
        if start not in self.adjList:
            return []  

        queue = Queue(queue_capacity)
        queue.enqueue(start)
        visited = set([start])
        traversal = []  

        while not queue.isEmpty():
            node = queue.dequeue()  
            if node is None:
                continue  

            traversal.append(node)

            for neighbor in self.adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return traversal 


    def dfs(self, start, stack_capacity=10):
        """Depth-First Search using the Stack ADT"""
        if start not in self.adjList:
            return []
        stack = Stack(stack_capacity)
        stack.push(start)
        visited = set([start])
        traversal = []
        while not stack.isEmpty():
            node = stack.pop()
            traversal.append(node)

            for neighbor in sorted(self.adjList[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)
        return traversal
