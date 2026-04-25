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
public:
    ListNode* newHead = nullptr;
    ListNode* newTail = nullptr;
    void helper(ListNode* head){
        if(!head){
            return;
        }
        reverseList(head->next);
        ListNode* nnode = new ListNode(head->val);
        if(!newHead && !newTail){
            newHead = newTail = nnode;
        }
        else{
            newTail->next = nnode;
            newTail = nnode;
        }
    }
    ListNode* reverseList(ListNode* head) {
        helper(head);
        return newHead;
    }
};
