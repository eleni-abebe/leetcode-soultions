class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        
        
        for i in range(len(s)-2):
            if len(s[i:3+i])==len(set(s[i:3+i])):
                count+=1
                
        return count
        