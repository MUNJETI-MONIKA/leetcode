class Solution:
    def isValidSudoku(self,board):
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                cell=board[row][col]
                if cell==".":
                    continue
                box=(row//3)*3+(col//3)
                if cell in rows[row] or cell in cols[col] or cell in boxes[box]:
                    return False
                rows[row].add(cell)
                cols[col].add(cell)
                boxes[box].add(cell)
        return True