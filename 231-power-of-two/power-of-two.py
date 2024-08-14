class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        por=1
        i=1
        while por<=n:
            if por==n:
                return True
            por=2**i
            i+=1

        