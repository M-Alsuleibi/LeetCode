class Solution:
    # Tc = O(logn), Sc = O(1)
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False        


    def sumOfSquares(self, n: int) -> int:
        sum = 0

        while n:
            digit = n % 10
            #digit = digit ** 2
            sum += digit ** 2
            n = n // 10
        return sum        
