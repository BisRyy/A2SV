class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        c = nums1 + nums2
        c.sort()
        
        return c[(len(c)-1)//2] if len(c)%2==1 else (c[(len(c)-1)//2] + c[(len(c)-1)//2+1])/2