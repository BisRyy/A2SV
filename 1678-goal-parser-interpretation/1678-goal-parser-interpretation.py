class Solution:
    def interpret(self, command: str) -> str:
        
        index = 0
        answer = ""
        while index < len(command):
            if command[index] == '(':
                if command[index + 1] == ")":
                    answer += "o"
                    index+=2
                else:
                    answer += "al"
                    index+=4
            else:
                answer += command[index]
                index+=1
        return answer