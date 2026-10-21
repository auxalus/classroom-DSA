class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,newnode):
        if (self.head== None):
            self.head = newnode
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newnode

    def print(self):
        temp = self.head
        print("Singly Linked list")
        while(temp):
            print(temp.data, end  = " ")
            temp = temp.next

    def insert(self,newnode,pos):
        temp = self.head
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
            return
        else:
            p = 1
            while(p!=pos-1 and temp.next != None):
                temp = temp.next
                p+=1
            newnode.next = temp.next
            temp.next = newnode
            return

    def delneg(self):
            temp = self.head
            prev = None
            while(temp.data<0):
                self.head = self.head.next
                temp = self.head
                if temp == None:
                    return 
            while temp:
                if(temp.data<0):
                    prev.next = temp.next
                    t = temp
                else:
                    prev = temp
                temp = temp.next
                t = None
            temp = None
    
list = LinkedList()
list.append(Node(70))
list.append(Node(-90))
list.append(Node(12))
list.print()
list.insert(Node(98),4)
list.insert(Node(-12),1)
print("\n inserted values")
list.print()
print("\n negative deleted values")
list.delneg()
list.print()