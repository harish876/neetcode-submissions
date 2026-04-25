class Solution {
public:
    vector<string> getNeighbors(string word, unordered_set<string>& st) {
        vector<string> neighbors;
        for (int i = 0; i < word.size(); i++) {
            string tmp = word;
            for (char c = 'a'; c <= 'z'; c++) {
                tmp[i] = c;
                if (st.count(tmp) && tmp != word) {
                    neighbors.push_back(tmp);
                }
            }
        }
        return neighbors;
    }

    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> st(wordList.begin(), wordList.end());
        if (!st.count(endWord)) return 0;

        queue<pair<string, int>> q; // word, distance
        q.push({beginWord, 1});

        unordered_set<string> visited;
        visited.insert(beginWord);

        while (!q.empty()) {
            auto [word, dist] = q.front();
            q.pop();

            if (word == endWord) return dist;

            for (string neighbor : getNeighbors(word, st)) {
                if (!visited.count(neighbor)) {
                    visited.insert(neighbor);
                    q.push({neighbor, dist + 1});
                }
            }
        }

        return 0; // No valid transformation sequence found
    }
};
