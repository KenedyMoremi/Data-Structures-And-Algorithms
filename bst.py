class BinarySearchTree:

    def __init__ (self, data):
        self.left = None
        self.data = data
        self.right = None

    #For inserting elements into the tree
    def insert(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)

        elif (data > self.data):
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)

        return self
    
    #In order traversal
    def in_order_traversal(self):

        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
#Helper Function to create binary search tree from a list
def createTree(lis):
    root = BinarySearchTree(lis[0])

    for i in lis:
        root.insert(i)

    print(root.in_order_traversal())

createTree([10, 6, 15, 3, 8, 20, 12])