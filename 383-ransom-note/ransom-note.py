class Solution(object):
    from collections import Counter
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = Counter(magazine) 

        for ch in ransomNote:
            if hashmap[ch] > 0:
                hashmap[ch]-=1
            else:
                return False
        return True