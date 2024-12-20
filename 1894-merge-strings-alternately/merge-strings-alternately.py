class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
    
    
        merged = []
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])
    
    
        if len1 > len2:
            merged.append(word1[min_len:])
        else:
            merged.append(word2[min_len:])

    
        return ''.join(merged)