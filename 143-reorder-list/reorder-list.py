# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None


        node = None

        while list2:
            temp = list2.next
            list2.next = node
            node = list2
            list2 = temp

        res = ListNode()

        while node and head:
            res.next = head
            head = head.next
            res = res.next

            res.next = node
            node = node.next
            res = res.next

        if node:
            res.next = node
        elif head:
            res.next = head

        return res