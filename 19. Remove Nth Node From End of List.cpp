#include <iostream>
using namespace std;


// Definition for singly-linked list.
 struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };
 
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (n == 0)
        {
            return head;
        }
        ListNode * tmp, * newHead;
        tmp =newHead =  head;
        for (int i = 0; i < n; ++i)
        {
            head = head->next;
        }
        if (head == NULL)
        {
            return newHead->next;
        }

        while( head->next != NULL){
            tmp = tmp->next;
            head = head->next;
        }
        tmp->next = tmp->next->next;
        return newHead;
    }
};