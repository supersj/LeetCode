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
