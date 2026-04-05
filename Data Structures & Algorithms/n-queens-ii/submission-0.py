class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        directions = [(-1,0), (-1,-1), (-1,1)]
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            nonlocal result 
            if row == n:
                result += 1
                return
            
            for col in range(n):
                if isValid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
            #backtrack here
        

        def isValid(row, col):
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                while 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] == "Q":
                        return False
                    nr += dr
                    nc += dc
            return True 

        backtrack(0)
        return result 
            



        