''' A basic unbalanced binary search tree implementation in Python, 
    with the following functionalities implemented:
        - Insertion
        - Deletion
        - Inorder
        - Preorder
        - Postorder
'''

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
     
    def insertNode(self, data):
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insertNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insertNode(data)
        else:
            self.data = data

    def minValueNode(self, node):
        current = node

        while(current.left is not None):
            current = current.left

        return current

    def deleteElement(self, data):
        if self is None:
            return None
        
        if data < self.data:
            self.left = self.left.deleteElement(data)
        elif data > self.data:
            self.right = self.right.deleteElement(data)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            
            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.deleteElement(temp.data)

        return self

    def printPostorder(self):
        if self.left:
            self.left.printPostorder()
        if self.right:
            self.right.printPostorder()
        print(self.data, end=" ")

    def printPreorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.printPreorder()
        if self.right:
            self.right.printPreorder()
    
    def printInorder(self):
        if self.left:
            self.left.printInorder()
        print( self.data, end=" ")
        if self.right:
            self.right.printInorder()



if __name__ == "__main__":
    
    root = BinarySearchTree(input("Enter data to initate the tree: "))

    while True:
        print("Select the any option")
        print("[1] Insert Element")
        print("[2] Delete Element")
        print("[3] Print Inorder")
        print("[4] Print Preorder")
        print("[5] Print Postorder")
        print("[6] Exit")
        print("\n")
        i = int(input())
        print("\n")

        if i == 1:
            root.insertNode(input("Enter data you want to insert: "))
        elif i == 2:
            root.deleteElement(input("Enter data you want to delete: "))
        elif i == 3:
            root.printInorder()
            print("\n")
        elif i == 4:
            root.printPreorder()
            print("\n")
        elif i == 5:
            root.printPostorder()
            print("\n")
        elif i == 6:
            break
        else:
            print("Entered Option is Invalid\n")