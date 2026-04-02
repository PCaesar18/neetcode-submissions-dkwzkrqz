class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        def backtrack(r, c, current):
            if current == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[current] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            for row, col in directions:
                nr, nc = row + r, col + c
                if backtrack(nr, nc, current + 1):
                    return True
            visited.remove((r,c))
            return False

            # to return here

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True
        return False
        