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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int len = 0;
        ListNode* curr = head;
        while(curr){
            len++;
            curr = curr->next;
        }

        int position = len - n - 1; //go to one step before it
        if(position == -1){
            return head->next;
        }
        ListNode* tmp = head;
        while(position){
            tmp = tmp->next;
            position--;
        }
        ListNode* nodeToRemove = tmp->next;
        tmp->next = nodeToRemove->next;
        return head;
    }
};
