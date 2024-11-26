# [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75) `EASY`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We need to maintain a rolling window of requests to count only the ones that fall within the last 3000 milliseconds. 

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
# Code
```python3 []
class RecentCounter:
    def __init__(self):
        # Initialize an empty deque to store timestamps
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Add the current timestamp to the deque
        self.queue.append(t)
        
        # Remove timestamps outside the 3000ms window
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        # The size of the deque is the count of requests in the time window
        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

