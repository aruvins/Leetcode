# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        def get_kth_node(start: ListNode, k: int):
            while start and k > 0:
                start = start.next
                k -= 1

            return start

        while True:
            kth_node = get_kth_node(group_prev, k)
            if not kth_node:
                break
            group_next = kth_node.next

            prev, cur = kth_node.next, group_prev.next
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp

        return dummy.next