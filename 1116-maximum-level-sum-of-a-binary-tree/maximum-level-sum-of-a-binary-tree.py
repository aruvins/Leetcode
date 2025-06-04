# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = []
        if not root:
            return ans

        q = deque([root])

        while q:
            l = len(q)
            val = 0
            curSum = 0

            for _ in range(l):
                node = q.popleft()
                curSum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(curSum)

        return ans.index(max(ans)) + 1