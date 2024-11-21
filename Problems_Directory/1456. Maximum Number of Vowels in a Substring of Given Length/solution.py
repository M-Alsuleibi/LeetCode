class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Time : O(n), Memory: O(1)
        v = ('a', 'e', 'i', 'o', 'u')
        L = 0
        curCount = 0
        maxCount = 0
        for R in range(len(s)) :
            # Check if the window size exceeds `k`
            if R - L + 1 > k:
            # Remove the leftmost character from the current window
                if s[L] in v:
                    curCount -= 1
                L += 1  # Shrink the window from the left
            # Add the right character to the current window
            if s[R] in v :
                curCount += 1

            # Update the maximum vowel count
            maxCount = max(maxCount, curCount)        

        return maxCount
