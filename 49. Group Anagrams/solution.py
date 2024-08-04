class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The approach is to create a dictionary with a map of counting char for each string
        # as a KEY and a list of string that match this count as a VALUE
        # e.g. { {a : 1, t : 1, e : 1} : ["ate", "eat", "tea"] } for  Input: strs = ["eat","tea","tan","ate","nat","bat"]
        # NOW hashmap is unhashable type so it can't be a KEY, this is why we convert it to tuple .Line #15
        # Tc = O(m * n) Sc = O(m * n)
        res = defaultdict(list) # mapping the countChat to list of anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s) 

        return res.values()    

