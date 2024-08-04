# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/submissions/1344485739/) `MEDIUM`

## Approach:
- The approach is to create a dictionary with a map of counting char for each string as a KEY and a list of string that match this count as a VALUE e.g. { {a : 1, t : 1, e : 1} : ["ate", "eat", "tea"] } for  Input: strs = ["eat","tea","tan","ate","nat","bat"] . 
NOW hashmap is unhashable type so it can't be a KEY, this is why we convert it to tuple .Line #15
- Time Complixity = O(m * n),  Space Complexity = O(m * n)
