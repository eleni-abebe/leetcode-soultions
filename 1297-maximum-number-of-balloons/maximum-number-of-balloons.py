class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = defaultdict(int)
        balloon = "balloon"
        
        for c in text:
            if c in balloon:
                counter[c] += 1
        
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])

        