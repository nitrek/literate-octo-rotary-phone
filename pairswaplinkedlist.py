

class Node:
    """
    A node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
    """
    A linked list implementation of a list.
    """
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        list = ""
        while temp:
            list = list + str(temp.data) + " "
            temp = temp.next
        print(list)
    def pairSwap(self):
      current = self.head
      temp = current.next
      current.next = current.next.next
      temp.next = current
      prev = current
      current = current.next
      
      self.head = temp
      while current.next:
        print("dd"+str(current.data))
        temp = current.next
        current.next = current.next.next
        temp.next = current
        current = current.next
        prev.next = temp
        self.printList()

llist = LinkedList()

llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printList()

print("swapping")

llist.pairSwap()

llist.printList()

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.push(9)
    llist.push(10)
    llist.printList()
    llist.pairSwap()
    llist.printList()