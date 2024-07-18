class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Tc = O(n)
        # Sc = O(n)
        map = {}

        for i in range(len(arr)):
            map[arr[i]]  = 1 + map.get(arr[i],0)

        valArr = map.values()

        if len(valArr) == len(set(valArr)):
            return True

        return False           
