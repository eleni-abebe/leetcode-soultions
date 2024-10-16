class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def shift(x, y):
            new_position = (ord(x) - ord('a') + y) % 26
            new_letter = chr(ord('a') + new_position)
            return new_letter

        arr = []
        for i in range(0, len(s), 2):
            arr.append(s[i])  
            if i + 1 < len(s) and s[i + 1].isdigit(): 
                shift_value = int(s[i + 1])  
                new_letter = shift(s[i], shift_value)
                arr.append(new_letter) 

        return ''.join(arr)