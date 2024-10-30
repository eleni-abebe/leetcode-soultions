class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
      
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            if sorted(temp) == temp:
                if len(set(temp)) == len(temp):
                    return True
        return False