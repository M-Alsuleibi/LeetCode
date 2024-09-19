class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # T O(n + m), M O(n) where n is 1st arg, m 2nd arg
        map = defaultdict(int)

        for c in stones:
            map[c] += 1
        count = 0

        for c in jewels:
            if map[c]:
                count += map[c]
        
        return count            
