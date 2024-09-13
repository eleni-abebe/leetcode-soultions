class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        copy=s[::-1]
        for i in range(len(s)): 
            s[i]=copy[i]
        