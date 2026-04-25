class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Each condition one by one
        """

        N = len(board)

        # 3 X 3 grid first
        for i in range(0,N-2,3):
            for j in range(0,N-2,3):
                st = set()
                for p in range(i,i+3):
                    for k in range(j,j+3):
                        if board[p][k] in st:
                            return False

                        elif board[p][k] != '.':
                            st.add(board[p][k])
        
        # row check
        for i in range(N):
            st = set()
            for j in range(N):
                if board[i][j] in st:
                    return False

                elif board[i][j] != '.':
                    st.add(board[i][j])

        # col check
        for i in range(N):
            st = set()
            for j in range(N):
                if board[j][i] in st:
                    return False

                elif board[j][i] != '.':
                    st.add(board[j][i])

        return True