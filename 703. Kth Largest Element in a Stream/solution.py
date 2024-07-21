class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initiate a minHeap with K  largest integers
        # length of nums can be LESS than k , so we cover it in add()
        self.minHeap , self.k = nums , k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # This condition cover the initializing of LESS than k
        if len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)
        return self.minHeap[0]    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
