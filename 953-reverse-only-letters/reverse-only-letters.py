class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        pt2 = len(s) - 1

        for pt1 in range(len(s)):
            if s[pt1].isalpha():
                while pt2 >= 0 and not s[pt2].isalpha():
                    pt2 -= 1
                arr.append(s[pt2])
                pt2 -= 1
            else:
                arr.append(s[pt1])

        return ''.join(arr)
            
        