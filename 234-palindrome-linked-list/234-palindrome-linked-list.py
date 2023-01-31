# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return head
        
        arr = [head.val]
        temp = head
        c = 0
        
        
        while temp.next:
            c+=1
            temp = temp.next
            arr.append(temp.val)
            
        return arr == arr[::-1]
        