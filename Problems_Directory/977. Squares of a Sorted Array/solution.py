class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Brute Force: square each number, Then sort the resultant array -> O(nlog)
        # Optimized(two pointers): Tc :O(2n) , Sc :O(n)
        
        L, R = 0, len(nums) - 1
        squaredNums = []
        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                squaredNums.append(nums[L]**2)
                L += 1
            else: 
                squaredNums.append(nums[R]**2)
                R -= 1
        return squaredNums[::-1]        

