# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        seen = set()
        cur = head
        seen.add(cur.val)

        while cur.next:
            if cur.next.val in seen:
                cur.next = cur.next.next
            else:
                seen.add(cur.next.val)
                cur = cur.next

        return head