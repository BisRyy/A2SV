class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        n = len(arr)
        i = 0
        while i < n:
            correct_position = arr[i] - 1
            if correct_position != i and arr[correct_position] !=0 :
                arr[correct_position], arr[i] = arr[i], arr[correct_position]
            else:
                i += 1
        print(arr)
        for i,num in enumerate(arr):
            if num != i+1:
                return i+1
        return 0