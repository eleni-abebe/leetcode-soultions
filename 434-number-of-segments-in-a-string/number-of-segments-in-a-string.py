class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segments = [segment for segment in s.split(' ') if segment]
        return len(segments)
        