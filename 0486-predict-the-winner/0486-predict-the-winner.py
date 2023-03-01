class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def fn(s,e,t):
            if s == e:
                if t:
                    return [nums[s], 0]
                else:
                    return [0, nums[s]]

            elif t:
                a1 = fn(s+1,e,not t)
                a1[0] += nums[s]
            
                a2 = fn(s,e-1,not t)
                a2[0] += nums[e]
                
                if a1[0] > a2[0]:
                    return a1
                else:
                    return a2
            
            else:
                a1 = fn(s+1,e,not t)
                a1[1] += nums[s]
                
                a2 = fn(s,e-1,not t)
                a2[1] += nums[e]
                
                if a1[1] > a2[1]:
                    return a1
                else:
                    return a2
                
        score = fn(0, len(nums)-1,True)
        return score[0] >= score[1]
        
        