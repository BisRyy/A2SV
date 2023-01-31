# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        arr = [head.val]
        temp = head
        c = 0
        
        
        while temp.next:
            c+=1
            temp = temp.next
            arr.append(temp.val)
            
        ans = []
        for i in arr:
            if i < x:
                ans.append(i)
                
        for i in arr:
            if i >= x:
                ans.append(i)
                
        temp = head
        for i in ans:
            temp.val = i
            temp = temp.next
        
        print(ans)
        return head
        