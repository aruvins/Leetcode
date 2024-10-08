# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000


# Solution:
# Grab the linked list and split it in half
# You basically have two linked lists now
# Reverse the links on the second list (second half) so you can grab it in order
# alternate between the two lists and append to a result list
# Input: head = [1,2,3,4,5] -> left = [1,2,3], right = [5,4]
# Then alternate through the left and right list -> res = [1,5,2,4,3]
# you can use a slow and fast pointer to find the middle

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        # reverse second portion of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs bgy alternating
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

