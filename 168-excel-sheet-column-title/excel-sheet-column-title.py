class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        mystr=""
        while columnNumber>0:
            mystr= chr(ord('A') + (columnNumber - 1) % 26) + mystr
            columnNumber = (columnNumber - 1) // 26
        return mystr
