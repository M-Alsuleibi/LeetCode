# [2446. Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/description/) `MEDIUM`
![Screenshot from 2024-11-10 16-34-54.png](https://assets.leetcode.com/users/images/50d2537f-89fb-4c55-9130-8add835e938d_1731249310.5253696.png)


# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Check which event comes before the other and compare between the `end` of the first event with the `start` of the second event.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
# Code
```python3 []
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        for i in range(2):
            if event1[0] < event2[0]:
                if event1[1] < event2[0] :
                    return False
                else:
                    return True

            else:
                if event2[1] < event1[0] :
                    return False
                else:
                    return True    
```
