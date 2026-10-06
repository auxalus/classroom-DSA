class Node:
    sum = 1
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def append(self, new_node):
        
        if self.head == None:
            self.head = new_node

        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node #appending the new node


    def print(self):
        temp = self.head
        while temp:
            if temp.data>0:
                sum += temp.data
            temp = temp.next
        print(sum)


list = LinkedList()
n1 = Node(11)
n2 = Node(22)
n3 = Node(33)
list.append(n1)
list.append(n2)
list.append(n3)

list.append(Node(44))