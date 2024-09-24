class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = max(nums)
        max_index = nums.index(max_value)

        for num in nums:
            if num != max_value and max_value < 2 * num:
                return -1

        return max_index
            