class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        arr=[]
        while l<r:
            if numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]==target:
                arr.append(l+1)
                arr.append(r+1)
                return arr
            else:
                r-=1
        
        