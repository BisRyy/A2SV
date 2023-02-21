# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        oddHead = ListNode()
        odd = oddHead
        
        while cur and cur.next:
            temp = cur.next
            cur.next = cur.next.next
            odd.next = temp
            temp.next = None
            odd = odd.next
            
            if cur.next:
                cur = cur.next
        if cur:
            cur.next = oddHead.next
        else:
            cur = oddHead.next
            
        return head
    
    
    
    
    