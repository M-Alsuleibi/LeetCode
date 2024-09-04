class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute Force -> Tc : O(nlogn)
        # Optimized:  Bucket Sort -> Tc : O(n), Sc : O(n)
        # array/bucket for count each value (0,1,2)
        count = [0, 0, 0]
        # Phase 1 : build the buckets
        for num in nums:
            count[num] += 1
        
        #Phase 2: rewrite the original array nums
        i = 0
        for k in range(len(count)):
            for _ in range(count[k]):
                nums[i] = k
                i += 1

        print(nums)        
           
