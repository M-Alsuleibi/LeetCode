
class MedianFinder:

    def __init__(self):
        self.small,self.large = [], []

    def addNum(self, num: int) -> None:
        # Nedd to handle 2 conditions : 
        # 1. small vaues < = large values
        # 2. abs(len(small) - len(large)) < = 1 
        # Start by pushing to one arbitrary heap, I choose the maxHeap(small numbers part)

        heapq.heappush(self.small, -1 * num)
        # Now handling the _ small vaues < = large values_ condition
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Handle uneven size 
        if len(self.small) > len(self.large) + 1: # Plus one so the size exceeds by 2 units or more
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1 * val)            

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
           return -self.small[0]
        elif len(self.large) > len(self.small) :
            return self.large[0]    
        # Even # of elements, return avg of two middle numbers 
        return (-1 * self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

