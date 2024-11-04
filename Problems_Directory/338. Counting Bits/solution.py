class Solution:
    def countBits(self, n: int) -> List[int]:
        # Brute Force: T O(nlogn), M O(1)
        res = [0] * (n + 1)
        for i in range(n + 1):
            count = 0
            j = i
            while j :
                count += j % 2 
                j = j // 2
            res[i] = count
            
        return res        
