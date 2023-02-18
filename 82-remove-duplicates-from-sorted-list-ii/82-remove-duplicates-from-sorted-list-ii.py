# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        a = []
        while curr:
            a.append(curr.val)
            curr = curr.next
        
        b = Counter(a)
        for i in b:
            if b[i] > 1:
                a = [j for j in a if j != i]
        if len(a)==0:
            return None
        curr = head
        for i in a:
            curr.val = i
            if i != a[-1]:
                curr = curr.next
        curr.next = None
        return head