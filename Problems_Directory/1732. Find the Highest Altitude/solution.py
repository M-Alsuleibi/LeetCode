class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = [0]
        total = 0

        for g in gain:
            total += g
            prefixSum.append(total)
        return max(prefixSum)    
