class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        if len(arr) < 2:
            return [] 

        arr.sort()
        dif = 0
        mndif = float('inf') 
        pairs = []

        for i in range(len(arr) - 1):  
            dif = abs(arr[i + 1] - arr[i])
            mndif = min(dif, mndif)

        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) == mndif:
                pairs.append((arr[i], arr[i + 1]))  
        return pairs

            