#Queue

class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


#Stack

class Stack:
    def __init__(self):
        self.items = []
      
    def push(self, item):
        self.items.append(item)
        print(self.items)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

#Queue using Stack

class QueueUsingStack:

    def __init__(self):
        self.stack = Stack()
    
    def enQueue(self,item):
      self.stack.push(item)

    def deQueue(self):
      self.reverseStack()
      item = self.stack.pop()
      self.reverseStack()
      return item
    
    def reverseStack(self):
      temp = Stack()

      while(not self.stack.isEmpty()):
        temp.push(self.stack.pop())
      
      self.stack = temp

    def isEmpty(self):
        return self.stack == []
    
    def size(self):
        return len(self.stack)

if __name__ == '__main__':
  q =Queue()
  q.enQueue('q1')
  q.enQueue('q2')
  q.enQueue('q3')

  while not q.isEmpty():
    print(q.deQueue())
  
  qus = QueueUsingStack()
  qus.enQueue('qus1')
  qus.enQueue('qus2')
  qus.enQueue('qus3')

  while not qus.isEmpty():
    print(qus.deQueue())

  s = Stack()
  s.push('s1')
  s.push('s2')
  s.push('s3')

  while not s.isEmpty():
    print(s.pop())
