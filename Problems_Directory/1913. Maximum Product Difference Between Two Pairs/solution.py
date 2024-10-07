class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        #Brute Force: T O(nlogn), M O(1)
        # Optomized: constructing min/max heaps with a cost of O(2 * n) to heapify it twice
        # T O(n), M O(n)
        minHeap = [ num for num in nums]
        maxHeap = [-num for num in nums]
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)
        w = x = y = z = 0
        w = heapq.heappop(minHeap)
        x = heapq.heappop(minHeap)
        y = - heapq.heappop(maxHeap)
        z = - heapq.heappop(maxHeap)
        return (y * z) - (w * x)
    
