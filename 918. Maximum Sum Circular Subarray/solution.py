class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Tc = O(n) , Sc = O(1)
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
        # If the globMax is non-positive, the whole array could be non-positive
        # Thus, the max subarray sum is the globMax itself

        # Otherwise, we compare the globMax vs. total sum minus globMin
        # The latter represents the maximum sum obtained by considering the circular nature of the array
        # We subtract globMin from the total sum to get the maximum sum subarray which wraps around the array
        return max(globMax, total - globMin) if globMax > 0 else globMax
