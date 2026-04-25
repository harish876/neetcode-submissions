/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
private:
    unordered_map<int,Node*>seen;
public:
    Node* cloneGraph(Node* node) {
        /*
            1 -> 2
            2 -> [1,3]
            3 -> [2]


            (1) -> []
            (2) -> [1,]
            (3) -> [2]

            (1) -> (2)
            (2) -> (1),(3)
            (3) -> (2)
        */

        if(!node){
            return nullptr;
        }

        else if(seen.find(node->val) == seen.end()){
            seen[node->val] = new Node(node->val);
        }

        for(Node* n: node->neighbors){
            if(seen.find(n->val) == seen.end()){
                seen[node->val]->neighbors.push_back(cloneGraph(n));
            }
            else{
                seen[node->val]->neighbors.push_back(seen[n->val]);
            }
        }
        
        return seen[node->val];
    }
};
