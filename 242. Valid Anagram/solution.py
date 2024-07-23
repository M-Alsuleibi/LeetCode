class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution #1
        # Brute Force using HashMap
        # Tc = O(s+t) , Sc = O(s+t)
        if len(s) != len(t):
            return False
            
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # Using .get() to avoid an error if s[i] is not a key yet   
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0): # Using .get() to avoid an error if c not found in countT
                return False

        return True           
        # Solution #2
        # Counter is a counting HashMap, using it here is kinda like cheatin LOL
        return Counter(s) == Counter(t)
        # Solution #3 , Tc = O(nlogn) BUT Sc = O(1)
        return sorted(s) == sorted(t)
