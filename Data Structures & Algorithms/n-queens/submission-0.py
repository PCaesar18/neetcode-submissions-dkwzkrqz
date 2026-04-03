class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # return all distinct solutions -> backtracking
        # we need directions 
        # n is number of queeuns as well as chessboard size 
        directions = [(-1,0), (-1,-1), (-1,1)]
        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if checkFree(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
        


        def checkFree(row, col):
            for dr, dc in directions:
                r, c = dr + row, dc + col
                while 0 <= r < n and 0 <= c < n:
                    if board[r][c] == "Q":
                        return False
                    r += dr
                    c += dc
            return True
        backtrack(0)
        return result 



        