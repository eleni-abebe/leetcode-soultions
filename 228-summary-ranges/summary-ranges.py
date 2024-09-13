class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        save = ""
        for i in range(len(nums)):
            if i<= len(nums) - 2 and nums[i+1] == nums[i] + 1:
                if save == "": save = str(nums[i]) + "->"
            else:
                ret.append(save + str(nums[i]))
                save = ""

        return ret  