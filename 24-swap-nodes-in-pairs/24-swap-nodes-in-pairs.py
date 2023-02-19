# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        fast = head
        slow = head.next
        
        while slow and fast:
            slow.val, fast.val = fast.val, slow.val
            
            if fast.next:
                fast = fast.next.next
            if slow.next:
                slow = slow.next.next
        
        return head