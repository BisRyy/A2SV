# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        maximum = 0
        rev = curr = head
        while curr:
            rev = rev.next
            curr = curr.next.next
        
        rev = reverseList(rev)
        
        while head and rev:
            maximum = max(head.val + rev.val, maximum)
            head = head.next
            rev = rev.next
        
            
        return maximum