class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        current = m + n -1

        
        while right >=0 and left >=0:
            if nums1[left] <= nums2[right]:
                nums1[current] = nums2[right]
                right-=1
                current-=1

            else:
                nums1[current] = nums1[left]
                left-=1
                current-=1

        # get leftovers
        while right >=0:
            nums1[current] = nums2[right]
            right-=1
            current-=1
