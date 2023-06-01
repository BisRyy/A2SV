class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = twenty = 0
        
        for bill in bills:
            if bill == 20:
                if ten > 0 and five > 0:
                    ten-=1
                    five-=1
                elif five > 2:
                    five-=3
                else:
                    return False
            elif bill == 10:  
                if five > 0:
                    five-=1
                else:
                    return False

            five += bill == 5
            ten += bill == 10
            twenty += bill == 20
        
        return True
            
            
            
        