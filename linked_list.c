//AN IMPROVED IMPLEMENTATION OF LINKED LISTS WITH SEPARATE FUNCTIONS FOR OPERATIONS//
#include<stdio.h>
#include<stdlib.h>
struct node{
	int i;
	struct node *link;
};
struct node *insertNodeEnd(struct node*, int);
struct node *insertNodeBeg(struct node *, int);
struct node *insertAfter(struct node*, int,int);
struct node *deleteNode(struct node*, int);
struct node *reverseList(struct node *head);
void displayList(struct node*);
void deleteList(struct node *);

int main(){
	struct node* head = NULL; //HEADER FOR LIST
	int n,data;
	printf("Enter the number of nodes you want to create: ");
	scanf("%d",&n);
	while(n--){
		printf("Enter the data: ");
		scanf("%d",&data);
		head = insertNodeEnd(head,data);
	}
	//head = insertNodeBeg(head,100);
	//displayList(head);
	//head = insertAfter(head,3,89);
	displayList(head);
	//head = deleteNode(head,5);
	head = reverseList(head);
	displayList(head);
	deleteList(head);
	return 0;
}

struct node *insertNodeEnd(struct node* head,int data){
	struct node* temp,p;
	temp = head;
	struct node* newNode = (struct node*)malloc(sizeof(struct node));
	newNode->i = data;
	newNode->link = NULL;
	if(head==NULL){
		head = newNode;	
	}else{
		while(temp->link!=NULL){
			temp=temp->link;
		}
		temp->link = newNode;
	}
	return head;
}
struct node *insertNodeBeg(struct node *head, int data){
	struct node *newNode = (struct node *)malloc(sizeof(struct node));
	newNode->link = head;
	newNode->i = data;
	head = newNode;
	return head;
}
struct node *insertAfter(struct node *head, int pos, int data){
	struct node *newNode = (struct node *)malloc(sizeof(struct node));
	struct node *temp = head;
	newNode->i = data;
	int i =0;
	while(i<(pos-1)){
		temp = temp->link;
		i++;
	}
	newNode->link = temp->link;
	temp->link = newNode;
	return head;
}
void displayList(struct node* head){
	struct node* temp;
	temp = head;
	if(temp!=NULL){
		printf("%d -> ",temp->i);
		displayList(temp->link);
	}
}
void deleteList(struct node *head){
	struct node *temp;
	while(head->link!=NULL){
		temp = head;
		free(temp->link);
		head = head->link;
	}
	free(head->link);
}
struct node *deleteNode(struct node* head, int pos){
	struct node *temp = head;
	struct node *pp = NULL;
		////// IF 1st node is deleted
	if(pos==1){
		head = head->link;
		free(temp);
	}else{
		int i = 0;
		while(i<(pos-2)){
			temp=temp->link;	
			i++;
		}
		if((temp->link)->link != NULL){
			pp = (temp->link)->link;
			free(temp->link);
			temp->link = pp;
		}else{
			free(temp->link);
			temp->link = NULL;
		}
	}	
	return head;
}
struct node *reverseList(struct node *curr){
	struct node *prev = NULL, *nextNode = NULL;
	while(curr){
		nextNode = curr->link;
		curr->link = prev;
		prev = curr;
		curr = nextNode;
	}
	return prev;
}