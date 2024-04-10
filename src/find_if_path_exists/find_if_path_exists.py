from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.create_graph(n, edges)
        return self.bfs(graph, source, destination)
    
    def create_graph(self, n: int,edges:  List[List[int]]) -> dict:
        graph = {i:[] for i in range(0,n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    
    def bfs(self,graph: dict, source: int, destination:int):
        visited = set()
        queue = [source]
        visited.add(source)
        while queue:
            s = queue.pop()
            if s == destination:
                return True
            for neigbour in graph[s]:
                if neigbour not in visited:
                    visited.add(neigbour)
                    queue.append(neigbour)
        return False
    

'''

time complexity is : O(m + n), where n is the number of nodes and m is the number of edges in the graph

Create Graph (create_graph method):
The time complexity of creating the graph is O(m), where m is the number of edges.

BFS Traversal (bfs method):
In the worst case, each node and edge are visited once, resulting in a time complexity of O(n + m).
The loop may iterate through all nodes and edges in the worst case, but each node is visited at most once.

----------------------------------------------------------

memory space : O(n + m)


Create Graph (create_graph method):
Since each node may have multiple neighbors, the space complexity for the graph representation is typically O(n + m), where n is the number of nodes and m is the number of edges.


BFS Traversal (bfs method):

The visited set in the bfs method is used to keep track of visited nodes during the BFS traversal. In the worst case, all nodes in the graph may need to be stored in the visited set, resulting in a space complexity of O(n).

The queue used for BFS traversal stores nodes to be visited. In the worst case, all nodes may need to be enqueued, resulting in a space complexity of O(n).



'''