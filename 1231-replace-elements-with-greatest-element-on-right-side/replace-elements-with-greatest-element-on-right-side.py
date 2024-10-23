class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        greatest = -1
        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = greatest  
            greatest = max(greatest, current)  
        return arr

        