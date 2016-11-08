#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode * result = head;

        int a[k];
        int i = 0;
        ListNode *p = head;
        while (head) {
            if (i != k)
            {
                a[i++] = head->val;
                head = head->next;
            }else
            {

                while (p != head) {
                    p->val = a[--i];
                    p = p->next;
                }
            }
        }
        return result;
    }
};

ListNode * create(int *a, int len) {
    ListNode * head = new ListNode(a[0]);
    ListNode * result = head;
    for (int i = 1; i < len; ++i)
    {
        head->next = new ListNode(a[i]);
        head = head->next;
    }
    return result;
}

void Print(ListNode *head) {
    while (head) {
        cout << head->val << endl;
        head = head->next;
    }
}

int main(int argc, char const *argv[])
{
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8};
    ListNode * h = create(a, 8);
    // Print(h);
    Solution ss;
    ListNode * re = ss.reverseKGroup(h, 3);
    Print(re);

    return 0;
}
