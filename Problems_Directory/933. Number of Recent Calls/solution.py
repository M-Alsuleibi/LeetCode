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
