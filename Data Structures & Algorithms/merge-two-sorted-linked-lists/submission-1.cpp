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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        while(list1 && list2){
            if(list1->val < list2->val){
                insert(list1->val);
                list1 = list1->next;
            }
            else if(list1->val > list2->val){
                insert(list2->val);
                list2 = list2->next;
            }
            else{
                insert(list1->val);
                insert(list2->val);
                list1 = list1->next;
                list2 = list2->next;
            }
        }
        while(list1){
            insert(list1->val);
            list1 = list1->next;
        }
        while(list2){
            insert(list2->val);
            list2 = list2->next;
        }
        return head;
    }
};
