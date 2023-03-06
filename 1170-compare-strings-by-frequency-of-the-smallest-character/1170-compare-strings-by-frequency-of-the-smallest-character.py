class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def freq(s):
            c = Counter(s)
            m = sorted(list(s))[0]
            return c[m]
        
        
        for idx, query in enumerate(queries):
            queries[idx] = freq(query)
            
        for idx, word in enumerate(words):
            words[idx] = freq(word)
            
        words.sort()  
        
        for idx, query in enumerate(queries):
            queries[idx] = len(words) - bisect_right(words, query)
        return queries
            