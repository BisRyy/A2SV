class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)+1
        arr = [0]+arr 
        ans  = [0]*n
        queue = deque([0])
                                                          
        for i in range(n):                                
            while arr[queue[0]] > arr[i]:
                queue.popleft() 
                                                          
            ans[i] = ans[queue[0]] + (i-queue[0]) * arr[i]  
            queue.appendleft(i)                           
                                                          
        return sum(ans) % (10**9 + 7)