# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        if not head.next and n == 1:
            head = head.next
            return head
        
        while temp.next:
            c+=1
            temp = temp.next
        temp = head
        
        if c+1 == n:
            head = head.next
            return head
            
        for i in range(c-n):
            temp = temp.next
        temp.next = temp.next.next
        
        return head
            
        