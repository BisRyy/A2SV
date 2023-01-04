class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        current_sum = 0
        answer = []
        
        for num in nums:
            if num % 2 == 0:
                current_sum += num
                
        for query in queries:
            index = query[1]
            change = query[0]
            
            before = nums[index]
            after = before + change
            nums[index] = after
            
            if before % 2 == 0 and after % 2 == 0:
                current_sum += change
                
            if before % 2 == 0 and after % 2 != 0:
                current_sum -= before
                
            if before % 2 != 0 and after % 2 == 0:
                current_sum += after
            answer.append(current_sum)
        return answer
                