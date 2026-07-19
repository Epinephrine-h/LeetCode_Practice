class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        res = []
        for c in s:
            if c == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        res.append(high)
        return res