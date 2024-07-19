class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute Force : Tc = O(nlogn), Sc = O(1)
       # nums.sort()
#
       # for i, num in enumerate(nums):
       #     if i != num :
       #         return i
#
       # return len(nums)  # In case missing number is outbound e.g. [0,1] , n == 2       

        # Optmized Solution: Tc = O(n) , Sc = O(1)      
        """
         using the mathematical formula for the sum of the first n natural numbers. 
         This approach avoids sorting and runs in linear time:
        """   
        
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
