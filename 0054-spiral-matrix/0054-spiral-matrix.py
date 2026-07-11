class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        r1, r2, c1, c2 = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for i in range(c1,c2 + 1):
                res.append(matrix[r1][i])
            r1 += 1
            for i in range(r1, r2 + 1):
                res.append(matrix[i][c2])
            c2 -= 1
            if c1 <= c2 and r1 <= r2:
                for i in range(c2, c1 - 1, -1):
                    res.append(matrix[r2][i])
                r2 -= 1
            if r1 <= r2 and c1 <= c2:
                for i in range(r2, r1 - 1, -1):
                    res.append(matrix[i][c1])
                c1 += 1
        return res
