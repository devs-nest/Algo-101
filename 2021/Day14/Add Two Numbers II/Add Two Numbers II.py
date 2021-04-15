# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        s1, s2 = 0, 0

        while l1 != None:
            s1 = s1*10+l1.val
            l1 = l1.next

        while l2 != None:
            s2 = s2*10+l2.val
            l2 = l2.next

        dummylist = dummy = ListNode(0)

        for i in str(s1+s2):
            dummy.next = ListNode(i)
            dummy = dummy.next

        return dummylist.next
