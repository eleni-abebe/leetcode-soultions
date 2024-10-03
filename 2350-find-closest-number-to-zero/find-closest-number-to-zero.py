class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=float('inf')
        for i in nums:
            k = abs(i)
            temp=min(temp,k)
        if -temp in nums and temp in nums:
            return temp
        elif -temp in nums and temp not in nums:
            return -temp
        else:
            return temp


        