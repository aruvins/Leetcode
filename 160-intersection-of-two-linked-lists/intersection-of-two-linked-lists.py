# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        firstSet = set()
        p1 = headA
        
        while p1:
            firstSet.add(p1)
            p1 = p1.next

        p2 = headB

        while p2:
            if p2 in firstSet:
                return p2
            p2 = p2.next

        return None

