
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = [None, None]
        def insert(word):
            curr = root
            for char in word:
                if not curr[int(char)]:
                    curr[int(char)] = [None, None]
                curr = curr[int(char)]
        
        def maxXOR(num1, num2, answer):
            nonlocal answers
            found = False

            if len(answer) == 32:
                answers.append(int(answer, 2))
                return

            for i in range(2):
                if num1[i] and num2[1-i]:
                    found = True
                    maxXOR(num1[i], num2[1-i], answer+"1")
            
            if not found:
                for i in range(2):
                    if num1[i]:
                        maxXOR(num1[i], num2[i], answer+"0")
        

        if len(nums) == 1:
            return 0
        
        for num in nums:
            insert(format(num, '032b'))
        answers = []
        
        maxXOR(root, root, "")
        return max(answers)

        