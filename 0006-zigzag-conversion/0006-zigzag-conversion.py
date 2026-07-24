class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:    return s
        ans = []
        for i in range(numRows):
            floor = i
            down = False if i != numRows - 1 else   True
            for j in range(i,len(s)):
                if floor == i:  ans.append(s[j])
                if down:  floor -= 1
                else:   floor += 1
                if floor == 0:  down = False
                if floor == numRows - 1:    down = True
        return "".join(ans)