class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            strr = ""
            for num in digits:
                strr += str(num)
            
            answer = []
            carry = 1
            for digit in reversed(strr):
                new_digit = (int(digit) + carry) % 10
                answer.append(new_digit)
                carry = (int(digit) + carry) // 10
            
            answer.reverse()
            if carry > 0:
                answer.insert(0, carry)
            return answer