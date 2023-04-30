class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = []
        m = [0,0]
        for i in range(2**len(nums)):
            temp = []
            for j in range(i.bit_length()):
                if 1 & i >> j == 1:
                    temp.append(nums[j])
            y = 0
            for x in temp:
                y|=x
            if y > m[0]:
                m = [y, 1]
            elif y == m[0]:
                m[1]+=1
        
        return m[1]