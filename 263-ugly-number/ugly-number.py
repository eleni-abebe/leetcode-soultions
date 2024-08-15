class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prm = [2, 3, 5]
        
        if n <= 0:
            return False
        
        for p in prm:
            while n % p == 0:
                n //= p
        
        return n == 1