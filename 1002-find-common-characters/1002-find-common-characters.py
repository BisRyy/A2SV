class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        letters = set(list(words[0]))
        commons = []
        
        for letter in letters:
            mincount = words[0].count(letter)
        
            for word in words:
                mincount = min(mincount, word.count(letter))
            
            for i in range(mincount):
                commons.append(letter)
        
        return commons