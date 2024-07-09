# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Phase 1: detect if there is a cycle vi slow and fast pointers
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break 

        # Cover the no cyle case
        if not fast or not fast.next:
            return None

        # Phase 2: detect cycle beginning via slow and slow2 pointers
        slow2 = head 
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow    

