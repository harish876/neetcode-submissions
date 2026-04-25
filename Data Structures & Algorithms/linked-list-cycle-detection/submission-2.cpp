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
    bool hasCycle(ListNode* head) {
        //fast slow pointer
        /*
            1   2   3   4
                        s
                        f
        */
        ListNode* fast = head && head->next ? head->next->next : nullptr;
        ListNode* slow = head;

        while(slow && fast){
            if(slow == fast){
                return true;
            }

            slow = slow->next;
            fast = fast->next && fast->next->next ? fast->next->next : nullptr;
        }
        return false;
    }
};
