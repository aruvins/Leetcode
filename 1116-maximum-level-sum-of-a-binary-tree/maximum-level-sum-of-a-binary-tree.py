from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []
        q = deque([root])
        maxSum = float('-inf')
        level = 1
        bestLevel = 1

        while q:
            curSum = 0

            for i in range(len(q)):
                node = q.popleft()
                curSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if curSum > maxSum:
                maxSum = curSum
                bestLevel = level
            level += 1

        return bestLevel

