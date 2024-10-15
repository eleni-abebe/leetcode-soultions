class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        arr=[]
        for char in address:
            if char=='.':
                arr.append('[.]')
            else:
                arr.append(char)
        return  ''.join(arr)