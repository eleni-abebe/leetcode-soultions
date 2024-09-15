class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        required = {}
        for char in t:
            required[char] = required.get(char, 0) + 1
        
        l, r = 0, 0
        min_len = float("inf")
        min_left = 0
        formed = 0
        window_c = {}
        
        while r < len(s):
            char = s[r]
            window_c[char] = window_c.get(char, 0) + 1
            
            if char in required and window_c[char]==required[char]:
                formed += 1
            
            while l <= r and formed == len(required):
                char = s[l]
                
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_left = l
                
                window_c[char] -= 1
                if char in required and window_c[char]<required[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if min_len == float("inf") else s[min_left:min_left + min_len]
        