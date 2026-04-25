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
    ListNode* head_ = nullptr;
    ListNode* tail_ = nullptr;
    void insert(int val){
        ListNode* nnode = new ListNode(val);
        if(!head_){
            head_ = tail_ = nnode;
        }
        else{
            tail_->next = nnode;
            tail_ = nnode;
        }
    }

public:
    void helper(ListNode* head){
        if(head == nullptr){
            return;
        }
        helper(head->next);
        insert(head->val);
    }
    ListNode* reverseList(ListNode* head) {
        helper(head);
        return head_;
    }
};
