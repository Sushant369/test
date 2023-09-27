class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


class LinkedList:
    def __init__(self):
        self.head=None
    
    #traverse
    def print_LL(self):
        if self.head is None:

            print("Linked list is Empty")
        else:
            n=self.head
            print(self.head)
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref
    
    #add_begining
    def add_begining(self,data):
        new_node = Node(data)
        new_node.ref=self.head
        self.head = new_node

    #add_end
    def add_end(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head=new_node
            # print(self.head)
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
                # print("ref: ",n)
            n.ref=new_node

    def insert_after(self,data,x):
        n = self.head

        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("LL is empty")
        else:
            new_node = Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def insert_before(self,data,x):

        if self.head is None:
            print("LL is empty")
            return

        if self.head.data==x:
            new_node = Node(data)
            new_node.ref=self.head
            self.head = new_node
            return
        n=self.head
        while n is not None:
            if n.ref.data == x:
                break
            n=n.ref

        if n is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_by_value(self,x):
        
        if self.head is None:
            print("Can't delete, linked list is empty")
            return
        
        if self.head.data ==x:
            self.head=self.head.ref
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref
        if n.ref is None:
            print("Can't find given value")
        else:
            new_ref=n.ref.ref
            n.ref.ref=None
            n.ref=new_ref






        



if __name__== '__main__':
    LL=LinkedList()
    # LL.add_begining(10)
    LL.add_end(20)
    LL.add_end(30)
    LL.insert_after(13,20)
    LL.insert_before(19,30)
    LL.delete_by_value(20)
    # LL.add_begining(11)
    LL.print_LL()
