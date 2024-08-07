class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Tc = O(2 * n) douvle for loop , Sc = O(1) bc its 26 lower case english characters

        count = defaultdict(int) # char -> count

        for c in s:
            count[c] += 1 # this throws error bc count[c] after = don't have value
                        # This is why using defaultdict(int) that initiates the map with ZERO

         # Here using enumerate inistead of using i to collect index
         # Then c = s[i]               
        for i,c in enumerate(s):
            if count[c] == 1:
                return i
        return -1           
