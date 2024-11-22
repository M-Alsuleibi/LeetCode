class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Result length 
        length = float('-inf')
        # Current window length
        windowLength = 0
        L = 0

        for R in range(len(nums)):
            if nums[R] != 1:
                L = R + 1
                windowLength = 0 # If find 0, then reset the window 
            if nums[R] == 1:
                windowLength += 1
                L += 1
            length = max(windowLength, length) 
        return length           
