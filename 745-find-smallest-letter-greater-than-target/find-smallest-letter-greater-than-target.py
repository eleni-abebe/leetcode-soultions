class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)-1
        while(left<=right):
            mid = (left+right)//2
            if(letters[mid]> target )and (letters[mid-1] <= target or mid==left):
                return letters[mid]
            elif letters[mid] > target:
                right = mid -1
            else:
                left = mid +1
        return letters[0]