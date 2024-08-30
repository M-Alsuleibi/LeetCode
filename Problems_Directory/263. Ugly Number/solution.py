class Solution:
    def isUgly(self, n: int) -> bool:
        # Tc = O(log n) , Sc = O(1)
        if n <= 0:
            return False

        for p in [2,3,5] :
            while n % p == 0 :
                n /= p   
        return n == 1 # if the condition is right will return True, otherwise False        
