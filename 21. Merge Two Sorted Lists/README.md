# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/) `EASY`
## My sloution that <code style="color : red">Time Limit Exceeded</code> : 
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=next1=list1
        cur2=next2=list2
        
 
        if not list1 or not list2:
            return list1 if list1 else list2

        while cur1 and cur2:
           if cur1.val <= cur2.val:
               next1 = cur1.next
               cur1.next = cur2
               next2 = cur2.next
               cur1 = next1
           else:
               cur2.next = cur1 
               cur2 = next2 

        if list1.val <= list2.val:
            return list1
        else:
            return list2
 
```
--- 
## `solution.py` Follow Dummy Node Approach
The approach using a dummy node is commonly referred to as the "Dummy Node" or "Sentinel Node" pattern. This technique is widely used in linked list problems to simplify edge case handling and streamline the code.

### Detailed Explanation of the Dummy Node Approach

#### Purpose

The dummy node serves as a placeholder at the beginning of the linked list, providing a non-null starting point. This helps to avoid special cases such as an empty list or the first insertion into the list, making the code cleaner and more manageable.

#### Steps

1. **Create a Dummy Node**: 
   - Initialize a dummy node that does not hold any meaningful data (often set to zero or another placeholder value).
   - Use a pointer (`tail`) that starts at the dummy node. This pointer will be used to build the merged list.

2. **Merge Lists**:
   - Traverse both input linked lists simultaneously.
   - At each step, compare the current nodes of the two lists.
   - Append the smaller node to the merged list by setting the `next` pointer of the `tail` to this node.
   - Move the pointer of the chosen list to the next node.
   - Move the `tail` pointer to the newly added node.

3. **Handle Remaining Nodes**:
   - Once one of the lists is exhausted, append the remaining nodes of the other list to the merged list.

4. **Return the Merged List**:
   - The merged list starts at the node following the dummy node (`dummy.next`), as the dummy node itself is just a placeholder.

#### Benefits

1. **Simplifies Edge Cases**:
   - Handles the case where one or both input lists are empty.
   - Avoids the need to write special cases for the first insertion into the merged list.

2. **Code Readability**:
   - The code is often easier to read and maintain because the dummy node provides a clear starting point.
   - The logic for handling the merging process remains straightforward and uniform.

3. **Robustness**:
   - Reduces the likelihood of null pointer exceptions by ensuring there is always a node to reference.

### Example

Here is a more detailed example using the dummy node approach to merge two sorted linked lists:

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node
        dummy = ListNode()
        # Tail pointer to build the new list
        tail = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move the tail pointer

        # Append remaining nodes
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Return the merged list starting from the node after the dummy
        return dummy.next
```

### Visualization

1. **Initial State**:
   - Dummy node (`dummy`) -> `None`
   - Tail pointer (`tail`) -> Dummy node

2. **Merging Process**:
   - Compare the values of the current nodes of `list1` and `list2`.
   - Append the smaller node to the list pointed to by `tail`.
   - Move the pointer of the chosen list forward.
   - Move the `tail` pointer to the newly added node.

3. **After Merging**:
   - The `dummy` node points to the head of the merged list.
   - Return `dummy.next` as the head of the merged list.

Using a dummy node ensures that you always have a non-null node to work with, which simplifies list manipulations and edge case handling.

## [YouTube - Leetcode Tricks - Dummy Nodes in Linked Lists (Python)](https://www.youtube.com/watch?v=-Cjgt5I0YvM)