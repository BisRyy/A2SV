class Solution:
    def calculate(self, s: str) -> int:
        nums=[]
        op='+'
        dig=0
        ans=0
        s=s.replace(' ','')
        for n,i in enumerate(s):
            if i.isdigit():
                dig=dig*10+int(i)
            if not i.isdigit() or n==len(s)-1:
                if op == '+':
                    nums.append(dig)
                elif op == '-':
                    nums.append(-1*dig)
                elif op == '*':
                    tmp=nums.pop()
                    nums.append(tmp*dig)
                elif op == '/':
                    tmp=nums.pop()
                    nums.append(int(tmp/dig))
                op=i
                dig=0
        while len(nums)>0:
            ans+=nums.pop()
        return ans