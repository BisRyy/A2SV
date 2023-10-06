class TrieNode:
    def __init__(self):
        self.childrens = [None]*26
        self.isEnd = False
        self.count = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        diff = val - self.map[key]
        self.map[key] = val
        for wordChar in key:
            asciiIndex = ord(wordChar) - ord('a')
            if not node.childrens[asciiIndex]:
                node.childrens[asciiIndex] = TrieNode()
            node = node.childrens[asciiIndex]
            node.count += diff
        node.isEnd = True
        

    def sum(self, prefix: str) -> int:
        cur=self.root
        for c in prefix:
            asciiIndex = ord(c) - ord('a')
            if not cur.childrens[asciiIndex]:
                return 0
            cur = cur.childrens[asciiIndex]
        return cur.count
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)