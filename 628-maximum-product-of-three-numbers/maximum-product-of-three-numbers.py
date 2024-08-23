class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product1=1
        product2=1
       
        nums.sort()
        n = len(nums)
        product1 = nums[n-1] * nums[n-2] * nums[n-3]
        product2 = nums[0] * nums[1] * nums[n-1]
        return max(product1,product2)