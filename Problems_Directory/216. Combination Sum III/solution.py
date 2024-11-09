class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = []

        def helper(i, curComb, curSum):
            if len(curComb) > k or curSum > n:
                return 
            
            if len(curComb) == k and curSum == n:
                combs.append(curComb[::])


            for j in range(i, 10):
                curComb.append(j)
                helper(j + 1, curComb, curSum + j) #recurse with next number
                curComb.pop() # Backtrack
                

        helper(1, [], 0)
        return combs

