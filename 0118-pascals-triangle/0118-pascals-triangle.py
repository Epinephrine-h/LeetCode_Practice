class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] for _ in range(numRows)]
        for i in range(1, numRows):
            tmp = []
            for j in range(1, len(ans[i - 1])):
                tmp.append(ans[i-1][j-1] + ans[i-1][j])
            tmp.append(1)
            ans[i] = ans[i] + tmp
        return ans 