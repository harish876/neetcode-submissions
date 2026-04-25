class ListNode {
    public:
        int val;
        ListNode* next;
        ListNode(int _val): val(_val){};
};

class LinkedList {
private:
    ListNode* head= nullptr;
    ListNode* tail = nullptr;
    int len;
public:
    LinkedList(): len(0) {}
    /*
        1 2
    */
    int get(int index) {
        if(index < 0 || index >= len){
            return -1;
        }
        ListNode* curr = head;
        int idx = 0;
        while(idx != index){
            idx++;
            curr = curr->next;
        }
        return curr ? curr->val : -1;

    }

    void insertHead(int val) {
        ListNode* nnode = new ListNode(val);
        len+=1;
        if(head == nullptr){
            head = tail = nnode;
        }
        else{
            nnode->next = head;
            head = nnode;
        }
    }
    
    void insertTail(int val) {
        ListNode* nnode = new ListNode(val);
        len+=1;
        if(tail == nullptr){
            head = tail = nnode;
        }
        else{
            tail->next = nnode;
            tail = nnode;
        }
    }

    bool remove(int index) {
        if(index >= len){
            return false;
        }

        if(index == 0){
            ListNode* nodeToDelete = head;
            head = head->next;
            delete nodeToDelete;
            len--;
            return true;
        }
   

        ListNode* curr = head;
        int idx = 0;
        while(idx < index-1){
            idx++;
            curr = curr->next;
        }
        ListNode* nodeToDelete = curr->next;
        ListNode* next = nodeToDelete ? nodeToDelete->next : nullptr;
        curr->next = next;
        if (index == len - 1) { 
            tail = curr;
        }

        delete nodeToDelete;
        len--;

        return true;
    }

    vector<int> getValues() {
        vector<int>result;
        ListNode* curr = head;
        while(curr){
            result.push_back(curr->val);
            curr = curr->next;
        }
        return result;
    }
};
