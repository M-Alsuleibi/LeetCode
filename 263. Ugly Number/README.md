# [263. Ugly Number](https://leetcode.com/problems/ugly-number/description/) `EASY`
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My thoughts circled around putting those three prime numbers _2_,_3_,_5_ in a set and checking if the number n has divisors among these three primes. If so return _True_ .But then I re-reaad the problem and dicover that my initial thought didn't cover the case of existing a prime among the divisors that is not one of them. e.g. n =14 , divisors are _2_,_7_. So accourding to my initial thought I have to return _True_ bc of _2_ as a divisor which is a wrong solution. 
# Approach
<!-- Describe your approach to solving the problem. -->
  The approch is 
- first to divide n by 2 as many times as we can ,
- then divide it by 3 as many times as we can,
- then divide it by 5 as many times as we can
- then if we able to reduce it to 1 then its an ugly number
- Otherwise return _False_
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O($$\log_{2} n$$), while the base is _2_ because if we suppose that _n_ is a huge integer e.g. $$2^{32}$$ , dividing it by _2_ will takes _32_ operations. Therefore $$\log_{2}$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O($1$)
# Code
```
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for p in [2,3,5] :
            while n % p == 0 :
                n /= p   
        return n == 1 # if the condition is right will return True, otherwise False        
```
