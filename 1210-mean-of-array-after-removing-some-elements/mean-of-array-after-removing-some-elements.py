class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        x = len(arr)//20
        return sum(arr[x:-x]) / (0.9 * len(arr))   
       