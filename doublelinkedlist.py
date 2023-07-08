class Node:
    def __init__(self, data, prev = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next


class doubleLinkedList:

    def __init__(self, head = None):
        self.head = head

    #find the length of the list
    def length(self):
        cont = 0

        #If the list is empty
        if(self.head == None):
            return 0

        else:
            node = self.head

            while node:
                cont += 1
                node = node.next
            
            return cont

    #Inserts element at the beginning of the list
    def insert_at_beginning(self, data):
        
        if self.head:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node
            return

        #If the list is empty
        self.head = Node(data)

    #Inserts element at the given index in the double linked list
    def insert_at(self, index, data):

        #Verify the index
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)

        else:
            node = self.head
            pos = 0

            while pos < (index - 1):
                pos += 1
                node = node.next
            
            new_node = Node(data, node, node.next)
            node.next.prev = new_node
            node.next = new_node
        
    #Insert element at the end of the list
    def insert_at_end(self, data):

        #If list is empty
        if self.head == None:
            self.insert_at_beginning(data)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(data, node, None)

    #Deletes the first Element in the double linked list
    def delete_first(self):

        #If the list is empty
        if self.head == None:
            raise Exception("The list is Empty")

        #If list has only head
        if self.length() == 1:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    #Deletes the specified node
    def delete(self, node_data):

        #If the list is empty
        if self.head == None:
            raise Exception("The list is Empty")

        node = self.head
        while node:
            #If the current node is the node to be deleted
            if node.data == node_data:
                break

            node = node.next
        
        #If this is the last Node
        if node.next == None:
            node.prev.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    #Deletes the last node
    def delete_last(self):

        #If the list is empty
        if self.head == None:
            raise Exception("The list is Empty")

        #If list has only head
        if self.length() == 1:
            self.head = None
            return

        node = self.head

        while node.next:
            node = node.next

        node.prev.next = None

    #Turns the double linked list into a list
    def to_list(self):
        node = self.head
        ls = []

        while node:
            ls.append(node.data)
            node = node.next

        return ls

    #Creates a double linked list from python list
    def from_list(self, python_list):

        for element in python_list:
            self.insert_at_end(element)

    #prints the elements
    def print_forward(self):
        
        arr = self.to_list()
        ls = ""

        for i in arr:
            ls += str(i) + "-->"

        print(ls)

    #traverse backwards
    def print_backward(self):

        arr = self.to_list()[::-1]      #reverse the list
        ls = ""

        for i in arr:
            ls += str(i) + "-->"

        print(ls)

