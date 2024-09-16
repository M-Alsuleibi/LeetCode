class Solution:
    def scoreOfString(self, s: str) -> int:
        # T O(n), M O(n)
        map = defaultdict(int)
        for c in s:
            map[c] = ord(c)
        # h e l l o 
        score = 0
        for i in range(len(s) - 1):
            score += abs(map[s[i]] - map[s[i + 1]])

        return score            
