# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Tc = O(n), Sc = O(n)
        
        # All elements in nums are unique.
        # Build hashSet
        nums = set(nums)
        dummy = ListNode(0,head)
        # dummy.next = head
        prev = dummy 
        cur = head # or dummy.next

        # while cur bc its the value to remove in found
        while cur: 
            if cur.val in nums:
                prev.next = cur.next
            else:
                prev = prev.next
            
            cur = cur.next
            
        return dummy.next            

