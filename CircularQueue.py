class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size ## fixed sized list
        self.front=-1
        self.rear=-1

    def enqueue(self,item):
        if (self.rear+1)%self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1: ## first insertion
            self.front=0

        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=item
        print(f"inserted : {item}")


    def dequeue(self):
        if self.front == -1:
            print("queue is empty")
            return None

        removed=self.queue[self.front]
        self.queue[self.front]=None


        if self.front == self.rear:
            self.front=self.rear=-1


        else:
            self.front=(self.front+1)%self.size


        print(f"removed element : {removed}")


    def peek(self):
        if self.is_empty():
            return "queue is empty"

        return self.queue[self.front]






    def is_full(self):
        return (self.rear+1)%self.size == self.front


    def is_empty(self):
        return self.front == -1


    def display(self):
        if self.is_empty():
            print( "queue is empty")
            return

        print("circular queue:",end=" ")
        i=self.front
        while True:
            print(self.queue[i],end=" ")
            if i == self.rear:
                break
            i=(i+1)%self.size

        print()




cq=CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

cq.enqueue(90)

cq.display()


cq.dequeue()
cq.enqueue(305)

cq.display()
            

    
            

        
        
