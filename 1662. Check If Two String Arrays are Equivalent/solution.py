class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp1=''
        temp2=''
        for word in word1:
            temp1 += word
        for word in word2:
            temp2 += word    
        if temp1 == temp2 : 
            return True
        return False        