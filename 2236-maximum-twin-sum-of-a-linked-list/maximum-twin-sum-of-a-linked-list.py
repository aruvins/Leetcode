# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        node = head
        res = 0

        while node:
            arr.append(node.val)
            node = node.next

        n = len(arr) - 1
        for i in range(len(arr)//2 + 1):
            res = max(res, arr[i] + arr[n-i])

        return res
        