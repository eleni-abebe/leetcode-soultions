class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        l=0
        r=len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                arr.append(nums[l]**2)
                l+=1
            else:
                arr.append(nums[r]**2)
                r-=1
        arr.reverse()
        return arr

        