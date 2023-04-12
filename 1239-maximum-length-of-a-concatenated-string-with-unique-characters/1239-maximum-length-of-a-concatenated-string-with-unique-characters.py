class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def intersect(charset,s):
            prev=set()
            for letter in s:
                if letter in prev or letter in charset:
                    return True
                prev.add(letter)
            return False
        
        charset=set()
        
        def backtrack(i):
            if i==len(arr):
                return len(charset)
            res=0
            
            if not intersect(charset,arr[i]):
                for letter in arr[i]:
                    charset.add(letter)
                res=backtrack(i+1)
                for char in arr[i]:
                    charset.remove(char)
                    
            return max(res,backtrack(i+1))
        
        return backtrack(0)
