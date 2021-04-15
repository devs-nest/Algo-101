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
class Solution
{
public:
    int add(ListNode *one, ListNode *two, int sone, int stwo, ListNode *&t)
    {
        if (sone == 0 && stwo == 0)
            return 0;
        int carry;
        int t1 = 0, t2 = 0;
        if (sone > stwo)
        {
            carry = add(one->next, two, sone - 1, stwo, t);
            t1 = one->val;
        }
        else if (sone < stwo)
        {
            carry = add(one, two->next, sone, stwo - 1, t);
            t2 = two->val;
        }
        else
        {
            carry = add(one->next, two->next, sone - 1, stwo - 1, t);
            t1 = one->val;
            t2 = two->val;
        }
        int data = t1 + t2 + carry;
        ListNode *nn = new ListNode(data % 10);
        nn->next = t;
        t = nn;
        return data / 10;
    }

    ListNode *addTwoNumbers(ListNode *one, ListNode *two)
    {
        ListNode *t = one;
        int sone = 0;
        while (t != NULL)
        {
            sone++;
            t = t->next;
        }
        t = two;
        int stwo = 0;
        while (t != NULL)
        {
            stwo++;
            t = t->next;
        }
        t = NULL;
        int carry = add(one, two, sone, stwo, t);
        if (carry)
        {
            ListNode *nn = new ListNode(carry);
            nn->next = t;
            t = nn;
        }
        return t;
    }
};