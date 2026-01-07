# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeSum(self, node):
        if not node:
            return 0
        return node.val + self.treeSum(node.left) + self.treeSum(node.right)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans = -1
        self.sum = self.treeSum(root)

        def post(node):
            if not node:
                return 0
            l = post(node.left)
            r = post(node.right)
            top = self.sum - (l + r)
            bigProduct = max((l + top) * r, (r + top) * l)
            self.ans = max(self.ans, bigProduct)
            return (l + node.val + r)
        post(root)
        return (self.ans % 1000_000_007)

        