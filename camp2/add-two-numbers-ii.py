# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = self.getLen(l1)+1
        len2 = self.getLen(l2)+1

        while len1 > len2:
            node = ListNode(0, l2)
            l2 = node
            len2 += 1

        while len1 < len2:
            node = ListNode(0, l1)
            l1 = node
            len1 += 1

        lead = self.Sum(l1, l2)

        if lead:
            node = ListNode(lead, l2)
            return node
        return l2

    def Sum(self, node1, node2):
        if not node1 or not node2:
            return 0

        lead = self.Sum(node1.next, node2.next) 
        sm = (node1.val + node2.val + lead) % 10
        lead = (node1.val + node2.val + lead) // 10
        node2.val = sm

        return lead

        

    def getLen(self, node):
        len_ = 0
        while node.next:
            len_ += 1
            node = node.next
        return len_
        
        