class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numb=(num-1)%9 +1
        if num>0:
            return numb
        else:
            return 0
        