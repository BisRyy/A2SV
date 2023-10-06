class TrieNode:
    def __init__(self):
        self.childrens = [None]*26
        self.isEnd = False
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, key: str) -> None:
        node = self.root
        for wordChar in key:
            asciiIndex = ord(wordChar) - ord('a')
            if not node.childrens[asciiIndex]:
                node.childrens[asciiIndex] = TrieNode()
            node = node.childrens[asciiIndex]
        node.isEnd = True
    
    def search(self, key):
        node = self.root
        for wordChar in key:
            asciiIndex = ord(wordChar) - ord('a')
            if not node.childrens[asciiIndex]:
                return False
            node = node.childrens[asciiIndex]
        return node.isEnd
        
        
class Solution:
        
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        t = Trie()
        ans = [0, ""]
        
        for word in words:
            n = len(word)
            if n == 1:
                t.insert(word)
                if ans[0] == 0:
                    ans = [1, word]
            else:
                if t.search(word[:-1]):
                    if ans[0] < n:
                        ans = [n, word]
                    t.insert(word)
        return ans[1]
            
        
        