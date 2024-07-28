class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute-force: nested for loops , and collect currentSum for each subarray
        # and compare it with maxSum , then return maxSum
        # Tc = O(n^2), Sc = O(1)

        # Optimized approach: Sliding window, Tc = O(n) , Sc = O(1)
        maxSum = float('-inf')
        curSum = 0
        L, R = 0, 0

        for R in range(len(nums)):
            if curSum < 0 :
                curSum = 0
                L = R
            curSum += nums[R]
            maxSum = max(maxSum, curSum)
            
        return maxSum    
