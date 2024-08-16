# Definition for singly-linked list.
class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1=l1
        temp2=l2
        a=[]
        b=[]
        c=[]
        while temp1 is not None:
            a.append(temp1.val)
            temp1=temp1.next
        while temp2 is not None:
            b.append(temp2.val)
            temp2=temp2.next
        a=a[::-1]
        b=b[::-1]
        aa=""
        for i in range(len(a)):
            aa+=str(a[i])
        ab=int(aa)
        bb=""
        for i in range(len(b)):
            bb+=str(b[i])
        ba=int(bb)
        cc=ab+ba
        st=str(cc)
        for i in range(len(st)-1,-1,-1):
            c.append(int(st[i]))
        temp3 = ListNode(c[0])
        ll = temp3
        

        for i in range(1, len(c)):
            new_node = ListNode(c[i])
            ll.next = new_node
            ll = ll.next

        return temp3
        