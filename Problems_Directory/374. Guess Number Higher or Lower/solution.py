# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Tc = O(logn), Sc = O(1)
        L, R = 1, n
        while L <= R:
            mid = (L+R) // 2
            result = guess(mid)
            if result < 0:
                R = mid - 1
            elif result > 0:
                L = mid + 1
            else :
                return mid        
        return -1
