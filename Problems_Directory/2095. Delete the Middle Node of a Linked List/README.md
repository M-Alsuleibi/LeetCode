# [2095. Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To identify the middle node efficiently, we can use the slow and fast pointer approach. This technique allows us to traverse the list only once while identifying the middle node.
# Approach
<!-- Describe your approach to solving the problem. -->
1. **Edge Case Handling**: 
   - If the list is empty (`head` is `None`), 
2. **Dummy Node**: 
   - Use a dummy node to simplify edge cases where the middle node might be the head.

3. **Slow and Fast Pointers**: 

   - Move the `slow` pointer one step and the `fast` pointer two steps in each iteration until the `fast` pointer or its `next` is `None`.

4. **Middle Node Deletion**:
   - After the loop, the `slow` pointer will be just before the middle node.
   - Update the `next` pointer of the `slow` pointer to skip the middle node.



# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$ single-pass traversal.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(1)$$

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow/fast pointers approach
        # T O(n), M O(1)
        if not head:
            return None

        dummy = ListNode(0, head)
        slow, fast = dummy, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return dummy.next
```
