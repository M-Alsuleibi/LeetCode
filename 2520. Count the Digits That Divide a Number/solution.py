class Solution:
    def countDigits(self, num: int) -> int:
        # Brute Force: collect all num digits in an array Then check if each digit divide num
        # Tc = O(n), SC = O(n).NOTE: num<= 10^9 so at max length of digit array will be 9
        # so we can assume its Sc = O(1) 
        # Optimized: not using extra memory for digits array
        # Tc = O(), Sc =O(1)
        
        count = 0 
        copy = num
        while copy > 0 :
            digit = copy % 10 
            copy = copy // 10
             # Avoid a division by zero and check if the digit divides 'num' without a remainder
            if digit != 0 and num % digit == 0 : 
                count += 1
        
        return count        

