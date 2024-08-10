# Definition for singly-linked list.

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        avr=head
        end=head
        while end is not None and end.next is not None:
            avr=avr.next
            end=end.next.next
        return avr

        