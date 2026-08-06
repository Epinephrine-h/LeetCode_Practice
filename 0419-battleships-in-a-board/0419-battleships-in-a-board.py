class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    ans+=1
                    if i < m - 1 and board[i+1][j] == "X":
                        for k in range(i+1,m):
                            if board[k][j] == ".":      break
                            board[k][j] = "."
                    elif j < n - 1 and board[i][j+1] == "X":
                        for k in range(j+1,n):
                            if board[i][k] == ".":      break
                            board[i][k] = "."
                    board[i][j] = "."
        return ans