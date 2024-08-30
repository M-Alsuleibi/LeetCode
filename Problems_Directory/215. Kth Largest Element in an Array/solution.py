class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Optimized way: Using heap(minHeap) of size k ,
        # return min in the minHeap is the kth largest elemnt
        # heapify(buid heap) : Tc = O(n)
        # return kth largest (min) : Tc = O(1)
        # Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate through the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:  # If the current element is larger than the smallest element in the heap
                heapq.heappushpop(min_heap, num)  # Push the current element and pop the smallest element
        
        # The root of the heap (the smallest element in the heap) is the k-th largest element
        return min_heap[0]
        
        
        
        # Naive way , Brute force : Tc = O(nlogn)
        # nums.sort()
        # return nums[-k]
        
