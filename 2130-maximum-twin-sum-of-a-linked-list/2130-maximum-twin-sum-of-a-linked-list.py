# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
            
        i = 0
        j = len(a)-1
        m = 0
        
        while i < j:
            m = max(m, a[i] + a[j])
            i+=1
            j-=1
            
        return m