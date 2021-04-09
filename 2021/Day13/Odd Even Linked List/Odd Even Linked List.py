# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        odd = head # Both of them point at the first node of the target linked list
        even = head.next # doesn't matter even there's only one node in the linked list (even will become None)
        eHead = even # We have to keep where the even-node list starts
        
        while even and even.next: # won't get in the loop at first if there's only one node in the linked list
            # both even and even.next are necessary condition because even might point to None, which has no attribute 'next'
            # AND, why these two, small discussion by myself as below
            odd.next = odd.next.next
            even.next = even.next.next
            # After these two ops, odd/even still points at its original place
            # Therefore, we move them to the next node repectively
            odd = odd.next
            even = even.next
        
        odd.next = eHead # the odd pointer currently points at the last node of the odd-node list
        
        return head # We keep the start of the odd-node list in the first of our code


#Four conditions I doubt for the while-loop:

#[A] odd and odd.next -> wrong when 1->2->3->4->None ( even nodes ) because even.next is None, which has no attribute 'next'
#[B] odd and even.next -> wrong when 1->2->3->4->5->None ( odd nodes ) because even is None, which has no attribute 'next'
#[C] even and odd.next -> wrong when 1->2->3->4->None ( even nodes ) because even.next is None, which has no attribute 'next'
#[D] even and even.next -> correct
#     (1). when 1->2->3->4->5->None ( odd nodes ) even will become None first and at the same time, odd points at the last node of the linked list; therefore, breaks from the while loop.
#     (2). when 1->2->3->4->None ( even nodes ) even.next will become None first and at the same time, odd points at the last-2 node of the linked list and even points at the last node of the linked list; therefore, breaks from the while loop.
