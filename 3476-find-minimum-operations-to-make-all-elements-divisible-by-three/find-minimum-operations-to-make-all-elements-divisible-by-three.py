class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            if nums[i]%3==0:
                continue
            else:
                count+=min(nums[i] % 3, 3 - (nums[i] % 3))
        return count


        