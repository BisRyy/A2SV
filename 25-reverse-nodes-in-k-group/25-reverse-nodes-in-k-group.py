# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        toReverse = ListNode()
        dummynode = toReverse
        
        ans = ListNode()
        curr = ans
        
        idx = 0
        node = head
        
        while node:
            
            if idx == k :
                reversednode = self.reverseList(toReverse.next)
                curr.next = reversednode
                
                while curr.next:
                    curr = curr.next
                    
                toReverse = ListNode()
                dummynode = toReverse
                idx = 0
                
            
            dummynode.next = ListNode(node.val,None)    
            dummynode = dummynode.next
            idx = idx + 1
            node = node.next
            
        
        if k == idx:
            reverseagain = self.reverseList(toReverse.next)
            curr.next = reverseagain

        else:
            curr.next = toReverse.next
                
        return ans.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,c = None, head
        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        return p