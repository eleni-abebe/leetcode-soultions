class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        count = 0
        for num in nums:
            if num != min_num:
                count += (num - min_num)
        return count