# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur:
            runner = cur

            while runner.next:
                if runner.next.val == cur.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            cur = cur.next

        return head