# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        arr = [head.val]
        temp = head
        c = 0
        
        while temp.next:
            c+=1
            temp = temp.next
            arr.append(temp.val)
            
        temp = head
        for i in arr[::-1]:
            temp.val = i
            temp = temp.next
            
        return head
            