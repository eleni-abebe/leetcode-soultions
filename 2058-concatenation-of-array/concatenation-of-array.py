class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        while len(ans)<2*len(nums):
            for i in nums:
                ans.append(i)
                
        return ans
       
        