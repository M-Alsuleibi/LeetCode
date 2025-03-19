# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
build a hash map of the index value of the foriegn dicttionary so we can know instantly if the words order is violated.
# Approach
<!-- Describe your approach to solving the problem. -->
There is two conditions to notice:
1. If one word is a prefix of another, the longer word should come after the shorter one.

2. If the characters at the same position in two words differ, their order should match the alien dictionary order.


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n+m)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
# Code
```python3 []
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count = {c:i for i, c in enumerate(order)}

        # Compare each pair of adjacent words
        for i  in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                # If w2 is shorter than w1 and all characters so far are equal, w2 should come after w1
                if j == len(w2):
                    return False
                # If characters differ, check their order in the alien dictionary
                if w1[j] != w2[j] :
                    if count[w2[j]] < count[w1[j]]:
                        return False
                    break # Move to the next pair of words

        return True                   
```
