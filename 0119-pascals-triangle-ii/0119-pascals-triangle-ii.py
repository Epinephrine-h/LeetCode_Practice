class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:    return [1]
        ans = [[1] for _ in range(rowIndex+1)]
        for i in range(1,rowIndex + 1):
            tmp = []
            for j in range(1,len(ans[i-1])):
                tmp.append(ans[i-1][j-1] + ans[i-1][j])
            tmp.append(1)
            ans[i] = ans[i] + tmp
        return ans[-1]