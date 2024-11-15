class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = [] # sublist of words
        self.count = 0 # counter not exceeds 3

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            if curr.count < 3:
                curr.words.append(word)
                curr.count += 1

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return [] #return empty list [] not empty string '' if prefix not found 
            curr = curr.children[c]
        return curr.words    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for p in products:
            trie.insert(p)
        res, curr = [], ''
        for c in searchWord:
            curr += c    
            res.append(trie.startsWith(curr))
        return res    
