class Solution:
    def decodeString(self, s: str) -> str: 
        
        stack = []
        
        for i in range(len(s)):
            
            if s[i] == ']':
                letters = ''
                nums = ''
                
                while stack and stack[-1] != "[":
                    letters+=stack.pop()
                    
                if stack[-1] == "[":
                    stack.pop()
                    
                while stack and stack[-1].isdigit():
                    nums+=stack.pop()
                    
                nums = int(nums[::-1]) if nums.isdigit() else 1
                letters = letters[::-1]
                
                new = nums *  letters
                stack += list( new ) if not new.isdigit() else []
                
            else:
                stack.append(s[i])
        ans = ""
        for i in stack:
            if not i.isdigit():
                ans+=i
        return ans