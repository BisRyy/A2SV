class Solution:
    def findComplement(self, num: int) -> int:
        for i in range( num.bit_length()):
            num = num|(1<<i) if num&(1<<i) == 0 else num&~(1<<i)
            
        return num