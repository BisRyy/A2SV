# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = head
        c = 0
        if not head:
            return head
        
        while temp.next:
            c+=1
            temp = temp.next
            
        temp = head
        k %= (c+1)
        if k == 0:
            return head
        
        temp1 = None
        temp2 = None
        
        for i in range(c-k):
            temp = temp.next
            
        temp1 = temp.next
        temp.next = None
        
        temp2 = head
        head = temp1
        
        while temp1.next:
            temp1 = temp1.next
            
        temp1.next = temp2
        
        return head
            
        
        
            