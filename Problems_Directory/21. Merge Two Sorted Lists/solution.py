# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         # Create a dummy node to act as the head of the merged list
        dummy = ListNode()
        tail = dummy

        # Traverse both lists and append the smaller value to the merged list
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # If any elements remain in either list, append them to the merged list
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Return the merged list, which starts at dummy.next
        return dummy.next
 
