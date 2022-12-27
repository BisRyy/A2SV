class Solution:
    def average(self, salary: List[int]) -> float:
        min_value = min(salary)
        max_value = max(salary)
        sum = 0

        for value in salary:
            if value not in(min_value, max_value):
                sum += value
        
        return sum / (len(salary) - 2)