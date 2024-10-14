class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-', '').upper()
        first_group_size = len(s) % k
        if first_group_size == 0:
            first_group_size = k
        result = []
        result.append(s[:first_group_size])
        for i in range(first_group_size, len(s), k):
            result.append(s[i:i + k])
        return '-'.join(result)

                    
