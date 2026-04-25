class Solution {
public:
    vector<vector<string>> result;

    string placeQueenAtIdx(int n, int idx) {
        string row(n, '.');
        row[idx] = 'Q';
        return row;
    }

    void dfs(int currRow, set<int>& cols, set<int>& leftDiag, set<int>& rightDiag, int n, vector<string>& acc) {
        if (currRow == n) {
            result.push_back(acc);
            return;
        }

        for (int col = 0; col < n; col++) {
            int leftDiagIdx = currRow - col;
            int rightDiagIdx = currRow + col;
            
            // Check if this column or diagonals are already occupied
            if (cols.count(col) || leftDiag.count(leftDiagIdx) || rightDiag.count(rightDiagIdx)) {
                continue;
            }

            // Place the queen and mark the column and diagonals as occupied
            acc.push_back(placeQueenAtIdx(n, col));
            cols.insert(col);
            leftDiag.insert(leftDiagIdx);
            rightDiag.insert(rightDiagIdx);

            // Recurse to the next row
            dfs(currRow + 1, cols, leftDiag, rightDiag, n, acc);

            // Backtrack: remove the queen and unmark the column and diagonals
            acc.pop_back();
            cols.erase(col);
            leftDiag.erase(leftDiagIdx);
            rightDiag.erase(rightDiagIdx);
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        result.clear();
        vector<string> acc;
        set<int> cols, leftDiag, rightDiag; // Track column, left diagonal, and right diagonal conflicts
        dfs(0, cols, leftDiag, rightDiag, n, acc);
        return result;
    }
};
