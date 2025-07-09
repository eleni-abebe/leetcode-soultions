class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
            if count % 3:
                result |= (1 << i)
        if result >= (1 << 31):
            result -= (1 << 32)
        return result