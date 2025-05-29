# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            stack = [root]
            leafArr = []

            while stack:
                v = stack.pop()
                if v:
                    if not v.left and not v.right:
                        leafArr.append(v.val)
                    else:
                        stack.append(v.left)
                        stack.append(v.right)

            return leafArr

        return dfs(root1) == dfs(root2)
