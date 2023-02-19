# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ""
        b = ""
        
        while l1: a = str(l1.val)+a;l1 = l1.next
        while l2:b = str(l2.val)+b;l2 = l2.next
        
        c = str(int(a) + int(b))
        print(c)
        head = None
        for i in c:
            new = ListNode(int(i))
            new.next = head
            head = new
        return head
            