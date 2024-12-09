# [2336. Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75) `MEDIUM`
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
# Code
```python3 []
class SmallestInfiniteSet:

    def __init__(self):
    # T O(n), S O(n)    
        self.heap = []
        for i in range(1,1001):
            self.heap.append(i)
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        # T O(1)
        if self.heap:
            return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        # T O(1)
        if num not in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```
