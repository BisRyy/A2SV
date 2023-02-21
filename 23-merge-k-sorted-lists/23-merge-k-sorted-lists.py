# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def insertionSortList(head):
            ans = ListNode(-float("inf"))
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

    
        ans = ListNode()
        curr = ans
        for node in lists:
            curr.next = node
            while curr.next:
                curr = curr.next
        
        return insertionSortList(ans.next)
        