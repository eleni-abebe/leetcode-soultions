# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        myarray=[]
        
        while head is not None:
            temp=head
            head=head.next
            temp.next=None
            myarray.append(temp.val)
        value=int("".join(str(x) for x in myarray), 2)
        return value


        