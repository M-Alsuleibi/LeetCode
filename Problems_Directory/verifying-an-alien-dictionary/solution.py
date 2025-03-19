class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count = {c:i for i, c in enumerate(order)}

        # Compare each pair of adjacent words
        for i  in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                # If w2 is shorter than w1 and all characters so far are equal, w2 should come after w1
                if j == len(w2):
                    return False
                # If characters differ, check their order in the alien dictionary
                if w1[j] != w2[j] :
                    if count[w2[j]] < count[w1[j]]:
                        return False
                    break # Move to the next pair of words

        return True                   
