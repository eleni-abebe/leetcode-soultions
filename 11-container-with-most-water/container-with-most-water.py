class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        maxa=0
        area=0
        while l<r:
            area=(r-l)*(min(height[l],height[r]))
            maxa=max(maxa,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxa





        