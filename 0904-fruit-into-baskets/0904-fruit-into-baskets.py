class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = Counter()
        left = right = max_num = 0
        while right < len(fruits):
            
            baskets[fruits[right]] += 1
            right += 1 
            
            while len(baskets) == 3:
                baskets[fruits[left]] -= 1 
                
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
                
            max_num = max(max_num, right - left)
            
        return max_num