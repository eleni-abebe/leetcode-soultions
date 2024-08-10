# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

       
        unique_vals = set()
        curr = head  
        prev = None  

      
        while curr:
           
            if curr.val in unique_vals:
                prev.next = curr.next
            else:
               
                unique_vals.add(curr.val)
                prev = curr
            curr = curr.next

        
        return head