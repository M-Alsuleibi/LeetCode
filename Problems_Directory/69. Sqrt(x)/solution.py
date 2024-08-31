class Solution:
    def mySqrt(self, x: int) -> int:
        # Brute Force: Tc = O(sqrt(x)), Sc = O(1)

        # Start checking from 0
        # for i in range(x + 1):
        #     # If i squared is greater than x, return the previous i
        #     if i * i > x:
        #         return i - 1
        # # If no number squared is greater, return x (which is 0 or 1)
        # return x
# -----------------------------------------------------------------------------------------------
        # Optimized: Binary Search. 

        # Since the search space is from 0 to i, take mid point M: if M^2 > x then reduce the search space to i to M .Iterrate
        # Tc = O(logn), Sc = O(1)
        L, R = 0, x 
        res = 0

        while L <= R:
            M = L + (R-L) // 2

            if (M * M) > x:
                R = M - 1
            elif (M * M) < x:
                L = M + 1
                res = M
            # not always execute    
            else:
                return M
 
        return res        
