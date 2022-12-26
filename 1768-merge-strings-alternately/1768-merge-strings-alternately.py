class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        answer = ""
        i = min(len(word1), len(word2))
        index = 0
        while index < i:
            answer += word1[index] + word2[index]
            index += 1
        answer += word1[index:] + word2[index:]
        return answer