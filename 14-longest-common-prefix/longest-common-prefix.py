class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest=min(strs,key=len)
        common_prifix=""
        for i,char in enumerate(shortest):
            for other in strs:
                if other[i]!=char:
                    return common_prifix
            common_prifix+=char
        return common_prifix
        