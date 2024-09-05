class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Brute Force: Convert to String
        # Tc: O(n), Sc: O(n)
        #if x < 0:
        #    return False
        # x = str(x)          # O(n) for String Conversion
        #return x == x[::-1]  # O(2*n) for String Reversal and Comparison
#-------------------------------------------------------------------------------------------
        # Optimized:
        # Tc: O(n), Sc: O(1)

        if x < 0:
            return False
        temp = x
        reverse = 0
        while temp != 0:
            digit = temp % 10 
            reverse = reverse * 10 + digit 
            temp //= 10
        # print(x == reverse)    
        return x == reverse    
