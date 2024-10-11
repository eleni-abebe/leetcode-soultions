class Solution(object):
    from collections import Counter
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_counter=Counter(magazine)
        for i in ransomNote:
            if mag_counter[i] >0:
                mag_counter[i]-=1
            else:
                return False
        return True

        


        