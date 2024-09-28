class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # T O(n), M O(1)
        L, R = 0, len(s) - 1
        while L <= R:
            temp = s[L]
            s[L] = s[R]
            s[R] = temp
            L += 1
            R -= 1