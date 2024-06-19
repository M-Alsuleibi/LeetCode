class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0   :
            return False
        if n == 1 : 
            return True
        while n > 1:
            n/=2
            if n.is_integer():
                continue
            else:
                return False
        return True                
