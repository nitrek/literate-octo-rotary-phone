


class Node:

  def __init__(self,key) -> None:
    
      self.data = key
      self.left = None
      self.right = None
      self.hd = 0
def printqueue(q):

  for i in q:
    print(i.data)
def levelOrder(root):
    
    q = []

    q.append(root)
 
    while(len(q)):
      #printqueue(q)
      current = q.pop(0)
      
      print("out"+str(current.data))

      if(current.left is not None):
        q.append(current.left)
      
      if(current.right is not None):
        q.append(current.right)

if __name__ == '__main__':
   
  root = Node(10)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(7)
  root.left.right = Node(8)
  root.right.right = Node(15)
  root.right.left = Node(12)
  root.right.right.left = Node(14)
  levelOrder(root)


  """
            10
      2           3   
    7   8       12   15
                    14 
  """