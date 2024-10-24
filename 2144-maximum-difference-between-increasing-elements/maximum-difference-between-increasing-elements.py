class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxm = -1 
        min_val = nums[0]  

        for j in range(1, len(nums)):
            if nums[j] > min_val:
                maxm = max(maxm, nums[j] - min_val)
            else:
                min_val = nums[j] 
        return maxm