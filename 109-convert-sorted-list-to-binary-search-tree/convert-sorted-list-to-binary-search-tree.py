# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next

            return length

        size = get_length(head)
        self.curr = head

        def build_tree(l,r):
            if l > r:
                return None

            mid = (l+r)//2

            left = build_tree(l, mid - 1)

            root = TreeNode(self.curr.val)
            root.left = left
            self.curr = self.curr.next

            root.right = build_tree(mid + 1, r)
            return root

        return build_tree(0, size - 1)