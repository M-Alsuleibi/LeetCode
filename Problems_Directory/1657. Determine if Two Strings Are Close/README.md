# [1657. Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75) `MEDIUM`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The two operations are almost meaningless, and you do not have to perform them at all to determine the answer.
# Approach
<!-- Describe your approach to solving the problem. -->
### Key Idea 
Two strings are "close" if:
1. They have the same characters. This is why make sets and compare `set1`, `set2`.
2. The counts of their characters can be matched after sorting. This is why make `count1`, `count2` arrays and compare them after sorting.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(nlogn)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
# Code
```python3 []
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # T O(nlogn), S O(n)
        map1, map2 = Counter(word1), Counter(word2)
        set1, set2 = set(word1), set(word2)
        count1, count2 = [], []

        if set1 != set2:
            return False

        for val in map1.values():
            count1.append(val)    
        for val in map2.values():
            count2.append(val)

        count1.sort()
        count2.sort()

        return count1 == count2


```
