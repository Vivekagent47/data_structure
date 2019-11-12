#include<stdio.h>
#include<stdlib.h>
typedef struct node{
	int data;
	struct node *next;
}node;
void push(node **top, int data){
	node *newNode = (node *)malloc(sizeof(node));
	if(!newNode){
		printf("\nSTACK OVERFLOW! HEAP FULL\n");
		return;
	}
	newNode->data = data;
	newNode->next = *top;
	*top = newNode;
}
int pop(node **top){
	if(!*top){
		printf("\nSTACK UNDERFLOW\n");
		return 0;
	}
	node *temp = *top;
	*top = (*top)->next;
	int data = temp->data;
	free(temp);
	return data;
}
void displayStack(node *head){
	node *temp = head;
	if(temp){
		printf("%d ",temp->data);
		displayStack(temp->next);
	}
}
int main(){
	node *stack=NULL;
	push(&stack,1);
	push(&stack,2);
	push(&stack,3);
	push(&stack,5);
	displayStack(stack);
	printf("\n");
	int data = pop(&stack);
	displayStack(stack);
	printf("\n");
	return 0;
}
