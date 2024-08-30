class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # To have the max diff : the first pair must be the largest, second pair must be the lowest
        # Largest pair value can be achived by choosing the largest and second large value in the array
        # Lowest pair value by doing the opposite
        
        # Time Complexity: O(NLogN)
        # phase 1
        nums.sort()
        a = nums.pop()
        b = nums.pop()
        # phase 2
        nums.reverse()
        c = nums.pop()
        d = nums.pop()

        return (a * b) - (c * d)

