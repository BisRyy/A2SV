class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        j = n
        i = 0
        for _ in range(n):
            ans.append(nums[i])
            ans.append(nums[j])
            j+=1
            i+=1
        return ans  
