class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count1 = 0
        count2 = 0
        mid = len(s) // 2

        for i in range(len(s)):
            if s[i].lower() in 'aeiou':
                if i < mid:
                    count1 += 1
                else:
                    count2 += 1

        return count1 == count2

                