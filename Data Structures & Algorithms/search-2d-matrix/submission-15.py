class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0,  ROWS * COLS -1

        while l <= r:
            mid = (l + r) // 2
            row = mid // COLS
            col = mid % COLS
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                l = mid + 1
            else:
                r = mid - 1
        return False



        