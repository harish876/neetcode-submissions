class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
            placement and backtracking right


            Q   .   .   .
            .   .   .   .
            .   .   .   .
            .   .   .   .

        """

        board = [['.'] * (n) for _ in range(n)]

        print([' '.join(b) for b in board])


        def can_place(i:int, j:int):
            # Check the row
            for col in range(n):
                if board[i][col] == 'Q':
                    return False

            # Check the column
            for row in range(n):
                if board[row][j] == 'Q':
                    return False

            # Check Diagonally (left up, right up, left down, right down)
            row, col = i,j
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False

                row -= 1
                col -= 1

            row, col = i,j
            while row < n and col < n:
                if board[row][col] == 'Q':
                    return False

                row += 1
                col += 1

            row, col = i,j
            while row >= 0 and col < n:
                if board[row][col] == 'Q':
                    return False

                row -= 1
                col += 1

            row, col = i,j
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False

                row += 1
                col -= 1
            
            return True


        result: List[List[str]] = []
        def helper(row: int):
            # Can i place something at (i,j) on the board
            if row >= n:
                result.append([''.join(b) for b in board])
                return

            for j in range(n):
                if can_place(row,j):
                    board[row][j] = 'Q'
                    helper(row+1)
                    board[row][j] = '.'


        helper(0)
        return result