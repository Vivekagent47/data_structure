class Node:
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeBeg(self, data):
        
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    def insertNodeEnd(self, data):
        newNode = Node(data)
        temp = self.head
        
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp

    def deleteNode(self, data):
        temp = self.head
        
        if(temp.next != None):
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    temp.previous.next = None
                    temp.previous = None
                return

        if (temp == None):
            return

    def printList(self):
        temp = self.head

        if self.head == None:
            print("Empty List")
        else:
            print("List : ", end=" ")
            while temp is not None:
                print(temp.data, end=" ")
                if temp.next:
                    print("-> ", end="")
                temp = temp.next
        print()
        

        
if __name__ == "__main__":
    lst = LinkedList()
    
    while True:
        print("Select the any option")
        print("[1] Insert Node at Beginning of List")
        print("[2] Insert Node at End of List")
        print("[3] Delete Node")
        print("[4] Print List")
        print("[5] Exit")
        print("\n")
        i = int(input())
        print("\n")

        if i == 1:
            lst.insertNodeBeg(input("Enter data you want to insert: "))
        elif i == 2:
            lst.insertNodeEnd(input("Enter data you want to insert: "))
        elif i ==3:
            lst.deleteNode(input("Enter data you want to delete: "))
        elif i == 4:
            lst.printList()
        elif i == 5:
            break
        
        print("\n")