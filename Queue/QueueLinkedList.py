#define node
class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enQ(self, data):
        n = node(data)
        if self.rear == None:
            self.front = self.rear = n
            return
        else:
            self.rear.next = n
            self.rear = n
            return

    def dQ(self):
        if self.front == None:
            return -1
        else:
            x = self.front.data
            self.front = self.front.next
            return x

    def disp(self):
        temp = self.front
        while temp != None:
            print(temp.data, end = ' ')
            temp = temp.next
        print()

q = Queue()
q.enQ(10)
q.enQ(20)
q.enQ(30)
q.disp()
q.dQ()
q.dQ()
q.disp()

