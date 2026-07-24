class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):     return s
        cur_row = 0
        direction = 0
        row = [""]*numRows
        for ch in s:
            row[cur_row] += ch
            if cur_row == 0:    direction = 1
            if cur_row == numRows - 1:   direction = -1
            cur_row += direction
        return "".join(row)