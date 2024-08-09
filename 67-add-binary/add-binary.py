
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1=int(a,2)
        num2=int(b,2)
        sum=num1+num2
        result=bin(sum)
        return result[2:]

        