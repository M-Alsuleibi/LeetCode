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
