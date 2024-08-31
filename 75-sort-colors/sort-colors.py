class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count1=0
        count2=0
        count3=0
        neww=[]
        for i in nums:
            if i==0:
                count1+=1
            elif i==1:
                count2+=1
            else:
                count3+=1
        index=0
        for _ in range(count1):
            nums[index] = 0
            index += 1
        for _ in range(count2):
            nums[index] = 1
            index += 1
        for _ in range(count3):
            nums[index] = 2
            index += 1