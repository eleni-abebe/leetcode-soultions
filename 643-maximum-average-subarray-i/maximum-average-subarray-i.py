class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        x=sum(nums[:k])
        y=x
       
        for i in range(len(nums)-k):
            x = x - nums[i] + nums[i + k]
            y=max(y,x)
        return float (y)/k
   