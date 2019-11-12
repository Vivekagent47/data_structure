#include<stdio.h>
#define MAX 100

void push(int data,int *stack, int *top){
	if(*top==MAX-1){
		printf("\nSTACK OVERFLOW\n");
		return;
	}
	stack[++(*top)] = data;
}
int pop(int *top, int *stack){
	if(*top==-1){
		printf("\nSTACK UNDERFLOW\n");
		return -1;
	}
	return stack[(*top)--];
}
void printStack(int *stack,int top){
	while(top>=0){
		printf("%d ",*(stack+top));
		--top;
	}
	printf("\n");
}
int main(){
	int stack[MAX],top=-1;
	push(1,stack,&top);
	push(2,stack,&top);
	push(3,stack,&top);
	push(5,stack,&top);
	printStack(stack,top);
	int data = pop(&top,stack);
	data = pop(&top,stack);
	printStack(stack,top);
	
	return 0;
}
