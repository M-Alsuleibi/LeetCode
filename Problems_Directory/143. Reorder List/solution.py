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
        slow ,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow2 = slow.next
        prev_node = slow.next = None
        while slow2:
            next_node=slow2.next
            slow2.next = prev_node
            prev_node=slow2
            slow2=next_node

        #merging two halves
        slow1 , slow2 = head , prev_node 
        while slow2: # because the second half maybe shorter 
            tmp1,tmp2 = slow1.next, slow2.next
            slow1.next = slow2
            slow2.next = tmp1
            slow1 = tmp1
            slow2 = tmp2
