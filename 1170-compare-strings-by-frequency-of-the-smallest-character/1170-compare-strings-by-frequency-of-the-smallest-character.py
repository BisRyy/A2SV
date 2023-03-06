class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def freq(s):
            m = min(s)
            return s.count(m)
        
        queries = [freq(query) for query in queries]
            
        words = sorted([freq(word)  for word in words])
    
        queries = [len(words) - bisect_right(words, query) for query in queries]
        
        return queries
            