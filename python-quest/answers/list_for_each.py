#Write your solution here
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    
    def __init__(self):
        self.head = None
        n1 = node(linked_list[0])
        self.head = n1
        for i in linked_list :

        


        # n2 = node(20)
        # n1.next = n2
        # n3 = node(30)
        # n2.next = n3
            pass
    def display(self):
        temp = self.head
        if self.head is None:
            print("EMPTY")
        while temp:
            print(temp.data)
            temp = temp.next

    def ListForEach():

        pass

linked = SLL()
linked_list = [1, 2, 3, 4, 5, 6]
linked.display()