class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        if len(tokens) == 1:
            return int(tokens[-1])
        
        for token in tokens:
            if token in ['+','-','*']:
                y = stack.pop()
                x = stack.pop()
                z = str(x) + str(token) + str(y)
                stack.append(eval(z))
            elif token == '/':
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(int(x/y))
            else:
                stack.append(token)
                
        return stack[-1]
                