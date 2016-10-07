#include <stdio.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode {
  int val;
  struct ListNode * next;
};
void deleteNode(struct ListNode* node) {
  if (node == NULL) {
    return ;
  }
  node->val = node->next->val;
  node->next = node->next->next;
}
void Print(struct ListNode* head){
  while (head!=NULL) {
    printf("%d    %p\n", head->val,head);
    head = head->next;
  }
}

struct ListNode* swapPairs(struct ListNode* head) {
  struct ListNode * cur,*tail;
  if (head==NULL || head->next ==NULL) {
    return head;
  }
  cur = head;tail = head->next;
  do{
    int tmp = cur->val;
    cur->val = tail->val;
    tail->val = tmp;
    if (!tail->next) {
      break;
    }
    cur = tail->next;
    tail = cur->next;
  }while(cur&&tail);
  return head;
}
// boolen hasCycle(struct ListNode *head) {
//   struct ListNode  *slow = head, *fast = head;
//
//     while ( fast && fast->next )
//     {
//         slow = slow->next;
//         fast = fast->next->next;
//         if ( slow == fast ) break;
//     }
//
//     return !(fast == NULL || fast->next == NULL);
// }

struct ListNode* createList(int elements[],int numbers){
  struct ListNode * start = NULL;
  struct ListNode * new_node, *cur;
  int i= 0;
  for ( i = 0; i < numbers; i++) {
    new_node = (struct ListNode *)malloc(sizeof(struct ListNode));
    new_node->val = elements[i];
    new_node->next = NULL;
    if (start == NULL) {
      start = new_node;
      cur = new_node;
    }else{
      cur->next = new_node;
      cur = new_node;
    }
  }
  Print(start);
  return start;
}

struct ListNode* reverseList(struct ListNode* head) {
  struct ListNode * pre,* aft;
  if (head == NULL || head->next == NULL) {
    return head;
  }
  pre = head;
  head = head->next;
  aft = head->next;
  pre->next = NULL;
  while(aft!=NULL){
    head->next = pre;;
    pre = head;
    head = aft;
    aft = aft->next;
  }
  head->next = pre;
  return head;
}


int main(int argc, char const *argv[]) {
  int elements[] = {1,2,3,4,5};
  struct ListNode * head  = createList(elements, 5);
  struct ListNode * revers = swapPairs(head);
  Print(revers);
  return 0;
}
