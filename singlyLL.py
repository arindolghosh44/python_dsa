class Node:
    def __init__(self,data):
        self.data=data
        self.next=None ## Pointer to the next Node


class SingleLL:
    def __init__(self):
        self.head=None

    def insertEnd(self,data):

        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return 

        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def insertB(self,data):

        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    
            
        
        
        
