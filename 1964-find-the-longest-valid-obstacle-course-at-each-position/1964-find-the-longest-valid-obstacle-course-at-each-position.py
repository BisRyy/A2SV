class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        answer = [1] * n
        list = []
    
        for i, height in enumerate(obstacles):
            idx = bisect.bisect_right(list, height)
            
            if idx == len(list):
                list.append(height)
            else:
                list[idx] = height
            answer[i] = idx + 1
            
        return answer