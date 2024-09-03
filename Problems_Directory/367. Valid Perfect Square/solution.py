class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Using binary search in range 1 to x -> Tc = O(logn), Sc = O(1)
        L, R = 1, num
        while L <= R :
            M = L + (R-L) // 2
            if M ** 2 > num : 
                R = M - 1
            elif M ** 2 < num:
                L = M + 1
            else :
                return True
        return False                

        
