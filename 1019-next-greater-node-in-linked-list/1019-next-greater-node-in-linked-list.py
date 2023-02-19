# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        curr = head
        
        while curr: 
            arr.append(curr.val)
            curr=curr.next
        
        s = []
        for i in range(len(arr)):
            while s and s[-1].get("value") < arr[i]:
                d = s.pop()
                arr[d.get("ind")] = arr[i]
            s.append({"value": arr[i], "ind": i})
            
        while s:
            d = s.pop()
            arr[d.get("ind")] = 0
        return arr
                