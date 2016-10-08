#include <stdio.h>
#include <stdlib.h>
typedef struct {
  int *elements;
  int size;
  int maxSize;
} Stack;

/* Create a stack */
void stackCreate(Stack *stack, int maxSize) {
  stack->elements = (int*)malloc(sizeof(int)*maxSize);
  stack->maxSize = maxSize;
  stack->size = -1;
}

/* Push element x onto stack */
void stackPush(Stack *stack, int element) {
  if (stack->size<stack->maxSize-1) {
    stack->size++;
    (stack->elements)[stack->size] = element;
  }else{
    return;
  }
}

/* Removes the element on top of the stack */
void stackPop(Stack *stack) {
  if (stack->size>=0) {
    stack->size--;
  }else{
    return;
  }
}

/* Get the top element */
int stackTop(Stack *stack) {
  if (stack->size == -1) {
    return 0;
  }
  return (stack->elements)[stack->size];

}

/* Return whether the stack is empty */
bool stackEmpty(Stack *stack) {
  if (stack->size == -1) {
    return true;
  }
  return false;
}

/* Destroy the stack */
void stackDestroy(Stack *stack) {
  free(stack->elements);
  stack->elements == NULL;
}
