class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertNodeBeg(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def insertNodeEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
    
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
    
    def deleteNode(self, data):
        temp = self.head
        
        if temp != None and temp.data == data:
            self.head = temp.next
            temp = None
            return
        while temp is not None:
            if temp.data == data:
                break
            prv = temp
            temp = temp.next
        
        if temp == None:
            return
        prv.next = temp.next
        temp = None       
            

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
        
        