# Count Connected Components
# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.

# Example 1:

# Input:
# n=3
# edges=[[0,1], [0,2]]
# Output:
# 1

# Example 2:

# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]
# Output:
# 2

# Constraints:
# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2

# Solution: Union find
# Imagine every node as its own graph with its parent being itself (for example: n=3, edges=[[0,1], [0,2]] -> graphs (0),(1),(2) each unconnected and has a parent being itself)
# loop through the edges and connect the nodes to its root parent (for example: graphs (0,1) (2) with 1 being connected to 0)
# next edges (for example: graphs (0,1,2) with 2 being connected to 0) 
# The find function below finds the root parent and the union function sets the parent of the specified node to the root
# since you're returning either 0 or 1 in union, subtract that from res (res should be the number of graphs, which starts at number of nodes and then decreases whenever a node is connected)

# for example: n=3, edges=[[0,1], [0,2]] -> graphs (0),(1),(2) -> res = 3
# for example: n=3, edges=[[0,1], [0,2]] -> graphs (0, 1),(2) -> res = 2
# for example: n=3, edges=[[0,1], [0,2]] -> graphs (0,1,2) -> res = 1

# for example: n=6, edges= [[0,1], [1,2], [2,3], [4,5]] -> graphs (0),(1),(2),(3),(4),(5) -> res = 6
# for example: n=6, edges= [[0,1], [1,2], [2,3], [4,5]] -> graphs (0,1),(2),(3),(4),(5) -> res = 5
# for example: n=6, edges= [[0,1], [1,2], [2,3], [4,5]] -> graphs (0,1,2),(3),(4),(5) -> res = 4
# for example: n=6, edges= [[0,1], [1,2], [2,3], [4,5]] -> graphs (0,1,2,3),(4),(5) -> res = 3
# for example: n=6, edges= [[0,1], [1,2], [2,3], [4,5]] -> graphs (0,1,2,3),(4,5) -> res = 2

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res