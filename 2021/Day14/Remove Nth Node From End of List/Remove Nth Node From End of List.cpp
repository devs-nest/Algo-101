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
        ListNode *ans,*slow=head,*fast=head;
        for(int i=0;i<n;++i) {
            fast=fast->next;
        }
        if(!fast) {  //delete first element
            ans=head->next;
            delete head;
            return ans;
        }
        while(fast->next) {
            slow=slow->next;
            fast=fast->next;
        }
        ans=slow->next->next;
        delete slow->next; 
        slow->next=ans;
        return head;
    }
};