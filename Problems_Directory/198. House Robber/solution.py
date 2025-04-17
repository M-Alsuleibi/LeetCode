class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        def bruteForce(ind):
            # memoization : O ()
            if memo[ind] != -1:
                return memo[ind]
            if ind == 0:
                return nums[0]
            if ind < 0:
                return 0

            rob = nums[ind] + bruteForce(ind-2)
            notRob = 0 + bruteForce(ind-1)

            memo[ind] = max(rob, notRob)
            return memo[ind]

        return bruteForce(len(nums)-1)            
