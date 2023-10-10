
class TrieNode:
    def __init__(self):
        self.pre={}
        self.suf={}
        self.index=set()

class Trie:

    def __init__(self):
        self.root1=TrieNode()

    def insert(self, word: str, index : int) -> None:
        cur=self.root1
        for c in word:
            if c not in cur.pre:
                cur.pre[c]=TrieNode()
            cur=cur.pre[c]
            cur.index = index
            
    
    def startsWith(self, prefix: str) -> bool:
        cur=self.root1
        for c in prefix:
            if c not in cur.pre:
                return -1
            cur=cur.pre[c]
        return cur.index 
    

class WordFilter:

    def __init__(self, words: List[str]):
        self.t = Trie()
        
        for index, word in enumerate(words):
            long = word + "#" + word
            for i in range(len(word)):
                self.t.insert(long[i:], index)

    def f(self, pref: str, suff: str) -> int:
         return self.t.startsWith(suff + "#" + pref)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)