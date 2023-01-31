# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        ans = []
        if not head or not head.next:
            return head
        while temp.next.next:
            if temp.val == temp.next.val:
                print(temp.val)
                temp.next = temp.next.next
                ans.append(temp)
            else:
                temp = temp.next
                ans.append(temp)
                
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        return head
                