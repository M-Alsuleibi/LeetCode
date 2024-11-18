class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # # Time : O(min(str1.length, str2.length)), Space: O(n)
        """ 
      ->  str1+str2 == str2+str1 if and only if str1 and str2 have a gcd .
E.g. str1=abcabc, str2=abc, then str1+str2 = abcabcabc = str2+str1
This(str1+str2==str2+str1) is a requirement for the strings to have a gcd. If one of them is NOT a common part then gcd is "".It means we will return empty string
Proof:-str1 = mGCD, str2 = nGCD, str1 + str2 = (m + n)GCD = str2 + str1

        """
  
        return str1[0: math.gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""  

