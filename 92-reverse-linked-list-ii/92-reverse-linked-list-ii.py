# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        arr = [head.val]
        temp = head
        c = 0
        
        left -= 1
        # right -=1
        while temp.next:
            c+=1
            temp = temp.next
            arr.append(temp.val)
            
        temp = head
        for i in arr[:left] + arr[left:right][::-1] + arr[right:]:
            temp.val = i
            temp = temp.next
            
        return head
            