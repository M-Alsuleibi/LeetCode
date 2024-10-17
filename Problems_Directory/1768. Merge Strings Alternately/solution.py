class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
	# T O(n), M O(n)
        s = ""
        l, r = 0, 0
        while True:
            if l < len(word1) and r < len(word2):
                s += word1[l] + word2[r]
                l += 1
                r += 1
            elif len(word1) > len(word2) and l < len(word1):
                s += word1[l]
                l += 1
            elif len(word1) < len(word2) and r < len(word2):
                s += word2[r]
                r += 1
            else:

                break    
        return s      
