class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Time: O(k * 2^n), Memory: O(n)
        combs = []
        
        # i is the individual number
        def helper(i, curComb):
            # 1st base case: curCumb > k
            if len(curComb) == k:
                combs.append(curComb[::]) # if we don't pass the copy the result(combs) will be [[],[],[],[],[],[]]
                return
            # 2nd base case: i > n
            if i >= n + 1:
                return
            # decision to include i
            curComb.append(i)
            helper(i + 1, curComb)
            # decision to NOT include i
            curComb.pop()        
            helper(i + 1, curComb)        

        helper(1, [])
        return combs    
