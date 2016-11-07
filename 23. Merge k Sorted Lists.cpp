#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* merge2Lists(ListNode*left, ListNode*right) {
        ListNode dummy(0);
        ListNode* tail = &dummy;

        while (left && right) {
            if (left->val < right->val)
            {
                tail->next = left;
                left = left->next;
            } else {
                tail->next = right;
                right = right->next;
            }
            tail = tail->next;
        }
        tail->next = left ? left : right;
        return dummy.next;
    }

    ListNode* mergeKListsHelp(vector<ListNode*>& lists, int l, int r) {
        int m = l + (r - l) / 2;
        if (l == r)
        {
            return lists[l];
        }
        if (l == r - 1)
        {
            return merge2Lists(lists[l], lists[r]);
        }
        return merge2Lists(mergeKListsHelp(lists,l,m),mergeKListsHelp(lists, m+1, r));
    }


    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int lenth = lists.size();
        if (lenth == 0)
        {
            return NULL;
        }
        return mergeKListsHelp(lists, 0, lenth-1);
    }
};

