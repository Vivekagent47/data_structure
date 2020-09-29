class Stack:
    def __init__(self):
        self.stack = list()
        
    def insertElement(self, data):
        self.stack.append(data)
    
    def deleteElement(self):
        print("Deleted element : ",self.stack.pop(), "\n\n")
    
    def printStack(self):
        print("Stack has elements : ", end=" ")
        for ele in self.stack:
            print(ele, end=", ")
        print("\n")
        
        
if __name__ == "__main__":
    lst = Stack()
    
    while True:
        print("Select the any option")
        print("[1] Insert Element")
        print("[2] Delete Element")
        print("[3] Print List")
        print("[4] Exit")
        print("\n")
        i = int(input())
        print("\n")

        if i == 1:
            lst.insertElement(input("Enter data you want to insert: "))
        elif i == 2:
            lst.deleteElement()
        elif i == 3:
            lst.printStack()
        elif i == 4:
            break
        