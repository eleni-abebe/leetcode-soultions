class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myary=[]
        unum=set(nums)
        n=len(nums)
        sum1=(n*n +n)//2
        sum2=sum(nums)
        duplicate = sum2 - sum(unum)
        myary.append(duplicate)
        myary.append(sum1-sum2+duplicate)
        return myary
        

        