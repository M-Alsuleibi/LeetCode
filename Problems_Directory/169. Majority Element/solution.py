class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Tc = O(n) , Sc = O(n)
        # integer division in python (or floor division)
        threshold = len(nums) // 2
        map = {}
        for num in nums:
            if num in map: 
                map[num] += 1
            else:
                map[num] = 1

        for num in nums:
            if map[num] > threshold:
                return num           
