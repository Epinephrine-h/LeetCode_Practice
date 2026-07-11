class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        one = 1
        while i >= 0 and one == 1:
            digits[i] += 1
            one -= 1
            if digits[i] == 10:
                digits[i] = 0
                one += 1
            i -= 1
        if one == 1:
            digits.insert(0,1)
        return digits