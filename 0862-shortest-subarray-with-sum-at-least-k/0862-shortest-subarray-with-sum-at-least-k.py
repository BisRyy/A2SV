class Solution:
    def shortestSubarray(self, A, K):
        
        Prefix = [0]*(len(A)+1)
        
        for i in range(len(A)):
            Prefix[i+1] = Prefix[i]+A[i]

        result = float("inf")
        Queue = deque()
        
        for i, curr in enumerate(Prefix):
            
            while Queue and curr <=  Prefix[Queue[-1]]:
                Queue.pop()
                
            while Queue and curr - Prefix[Queue[0]] >= K:
                result = min(result, i - Queue.popleft())
                
            Queue.append(i)
            
        return result if result != float("inf") else -1
