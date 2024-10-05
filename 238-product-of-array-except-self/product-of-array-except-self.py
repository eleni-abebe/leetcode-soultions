class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        lp = [1] * n
        right_product = 1

        for i in range(1, n):
            lp[i] = lp[i - 1] * nums[i - 1]

        for i in range(n - 1, -1, -1):
            lp[i] *= right_product
            right_product *= nums[i]

        return lp
        