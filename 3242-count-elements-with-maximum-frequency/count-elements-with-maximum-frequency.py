class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = Counter(nums)
        max_freq = max(frequency.values())
        total_freq = sum(count for count in frequency.values() if count == max_freq)
        return total_freq
    
        