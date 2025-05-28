# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(root,1)]
        
        while stack:
            v, depth = stack.pop()
        
            if v:
                max_depth = max(max_depth, depth)
                stack.append((v.left, depth + 1))
                stack.append((v.right, depth + 1))

        return max_depth
            


        