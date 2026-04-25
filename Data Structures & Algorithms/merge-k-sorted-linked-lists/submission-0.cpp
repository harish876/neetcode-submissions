/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
private:
    ListNode* head = nullptr;
    ListNode* tail = nullptr;
    
    void insert(int val){
        ListNode* nnode = new ListNode(val);
        if(!head){
            head = tail = nnode;
        }
        else{
            tail->next = nnode;
            tail = nnode;
        }
    }

public:
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val; // Min-heap: smaller values have higher priority
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        /*
            1
            1
            1
        */
        priority_queue<ListNode*,vector<ListNode*>,Compare>pq;
        for(auto listHead: lists){
            pq.push(listHead);
        }

        while(!pq.empty()){
            ListNode* top = pq.top();
            pq.pop();

            insert(top->val);

            if(top->next){
                pq.push(top->next);
            }
        }
        return head;
    }
};
