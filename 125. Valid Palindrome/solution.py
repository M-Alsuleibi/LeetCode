class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_string = ''.join(filter(str.isalnum,s))

        lower_alnumstring = alnum_string.lower()

        l,r = 0 , len(lower_alnumstring)-1

        while l < r :
            if lower_alnumstring[l] == lower_alnumstring[r]:
                l+=1
                r-=1
            else: 
                return False    
        return True     # if empty string do not enter the loop and return True   
