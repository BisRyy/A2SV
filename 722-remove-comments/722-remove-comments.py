class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        in_block = False
        new_line = ""
        
        for line in source:
            
            if not in_block:
                new_line = ""
            
            i = 0
            n = len(line)
            
            while i < n:
                
                if in_block:
                    
                    if line[i : i+2] == '*/' and i + 1 < n:
                        i+=2
                        in_block = False
                        continue
                        
                    i+=1
                    
                else:
                    
                    if line[i:i + 2] == '/*' and i + 1 < n:
                        i += 2
                        in_block = True
                        continue
                    
                    if line[i:i + 2] == '//' and i + 1 < n:
                        break
                    
                    new_line += line[i]
                    i += 1
                    
            if new_line and not in_block:
                answer.append(new_line)
                                
        return answer

    
        '''
            source = [
                        "/*Test program */",
                        "int main()",
                        "{ ", 
                        "  // variable declaration ", 
                        "int a, b, c;",
                        "/* This is a test",
                        "   multiline  ", 
                        "   comment for ",
                        "   testing */",
                        "a = b + c;", 
                        "}"
                    ]
                    
                [
                    "int main()",
                    "{ ","  ",
                    "int a, b, c;",
                    "a = b + c;",
                    "}"
                ]         
                
            source = [
                        "a/*comment", 
                        "line", 
                        "more_comment*/b"
                    ]
            
                    [
                        "ab"
                    ]
        '''
    