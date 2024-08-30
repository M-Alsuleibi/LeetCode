class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor

