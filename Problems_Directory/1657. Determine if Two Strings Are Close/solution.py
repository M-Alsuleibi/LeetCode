class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # T O(nlogn), S O(n)
        map1, map2 = Counter(word1), Counter(word2)
        set1, set2 = set(word1), set(word2)
        count1, count2 = [], []

        if set1 != set2:
            return False

        for val in map1.values():
            count1.append(val)    
        for val in map2.values():
            count2.append(val)

        count1.sort()
        count2.sort()

        return count1 == count2

