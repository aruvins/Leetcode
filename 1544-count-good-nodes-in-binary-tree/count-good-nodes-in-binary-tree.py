# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-inf'))]
        goodNodes = 0

        while stack:
            node, largest = stack.pop()

            if node:
                if largest <= node.val:
                    goodNodes += 1

                largest = max(largest, node.val)

                stack.append((node.left, largest))
                stack.append((node.right, largest))

        return goodNodes