
class TrieNode:
    def __init__(self):
        self.children={}
        self.count=0

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
                
            cur=cur.children[c]
            cur.count+=1    

    def search(self, word: str) -> bool:
        cur = self.root
        count = cur.count
        for c in word:
            cur = cur.children[c]
            count += cur.count
        return count
         
               
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.search(word))
        return ans
    
    