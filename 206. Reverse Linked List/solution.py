# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node=next_node = None
        curr=head
        while curr:
            next_node=curr.next
            curr.next = prev_node
            prev_node=curr
            curr=next_node
        head=prev_node
        return head