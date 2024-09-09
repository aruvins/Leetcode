# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

# Solution: DFS
# Input: prereq = [[0,1],[0,2],[1,3],[1,4],[3,4]]
# Create an adjacency list
#   Prereq Map
# --------------
#  crs  |  pre
# --------------
#   0   | [1,2] 
#   1   | [3,4] 
#   2   | [] 
#   3   | [4] 
#   4   | [] 
#
# Run DFS by starting at 0 and look at prereq [1,2]
# Run DFS on prereq 1 and run DFS on it's prereqs
# Continue until you run into a course with no prereqs and then you know it can be completed
# Then backtrack and remove the completed course from each course
# keep going like this until the original node has no prereqs
# Time: O(n + p) because you have to visit every node and edge
# If it is a loop then return false
# you can detect this by creating a set and keeping track of visited nodes in this set
# If you see that a node has been visited twice then return false 


from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            preMap[crs] = [] #makes it faster since it no longer needs to run through its' prereqs
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False #This is for the case if there is an unconnected graph
        return True
