# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-5001)
        while head:
            node, head = head, head.next
            node.next = None
            curr = ans
            while curr:
                if curr.val < node.val :
                    prev = curr
                    curr = curr.next
                else: break
            node.next, prev.next = prev.next, node
        return ans.next
