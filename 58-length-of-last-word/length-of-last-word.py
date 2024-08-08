class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        reversed_s = s[::-1]
        count = 0
        
        if reversed_s[0].isalnum():
            for char in reversed_s:
                if char.isalnum():
                    count += 1
                else:
                    break
        else:
            i = 0
            while i < len(reversed_s) and reversed_s[i] == ' ':
                i += 1
            for char in reversed_s[i:]:
                if char.isalnum():
                    count += 1
                else:
                    break
        
        return count