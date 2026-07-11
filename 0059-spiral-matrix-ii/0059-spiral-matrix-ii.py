class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        r1, r2, c1, c2, val = 0, n - 1, 0, n - 1, 1
        while r1 <= r2 and c1 <= c2:
            for i in range(c1, c2 + 1):
                res[r1][i] = val
                val += 1
            r1 += 1
            for i in range(r1, r2 + 1):
                res[i][c2] = val
                val += 1
            c2 -= 1
            if r1 <= r2 and c1 <= c2:
                for i in range(c2, c1 - 1, -1):
                    res[r2][i] = val
                    val += 1
                r2 -= 1
            if c1 <= c2 and r1 <= r2:
                for i in range(r2, r1 - 1, - 1):
                    res[i][c1] = val
                    val += 1
                c1 += 1
        return res
