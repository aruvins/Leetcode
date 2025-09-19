# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        remainder = 0
        prev = None

        while head1 or head2:
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0
            total = val1 + val2 + remainder

            remainder = total // 10
            new_val = total % 10

            if head1:
                head1.val = new_val
                prev = head1
                head1 = head1.next
            else:
                prev.next = ListNode(new_val)
                prev = prev.next

            if head2:
                head2 = head2.next

        if remainder:
            prev.next = ListNode(remainder)
        return l1

