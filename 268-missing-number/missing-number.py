class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        for i in range(0, n):
            if i not in nums:
                return i
        
        
        return n
        