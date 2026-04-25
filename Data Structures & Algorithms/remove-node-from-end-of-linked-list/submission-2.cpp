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
        //end of the list lol
        int len = 0;
        ListNode *temp = head;
        while(temp){
            temp = temp->next;
            len++;
        }

        if(!head){
            return head;
        }

        if(len-n == 0){
            head = head->next;
            return head;
        }

        
        ListNode* tmp = head;
        int idx = 0;
        while(idx < (len-n-1)){
            tmp = tmp->next;
            idx++;
        }

        ListNode* nodeToUnlink = tmp->next;
        if(!nodeToUnlink){
            return nullptr;
        }

        //std::cout << "Node to Unlink: " << nodeToUnlink->val << std::endl;
        ListNode* nextNode = nodeToUnlink->next;
        tmp->next = nextNode;
        nodeToUnlink->next = nullptr;

        delete nodeToUnlink;
        return head;
    }
};
