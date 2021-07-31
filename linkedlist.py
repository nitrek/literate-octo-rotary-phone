class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def getNth(self, index):
		current = self.head 
		count = 0
		while (current):
			if (count == index):
				return current.data
			count += 1
			current = current.next

		# if we get to this line, the caller was asking
		# for a non-existent element so we assert fail
		assert(false)
		return 0

	def reverse(self):
		current = self.head
		prev = None
		while (current):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev


	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next

# Driver Code
if __name__ == '__main__':

	llist = LinkedList()

	# Use push() to construct below list
	# 1->12->1->4->1
	llist.push(1)
	llist.push(4)
	llist.push(1)
	llist.push(12)
	llist.push(1)

	n = 3
	llist.printList()
	print("Element at index 3 is :", llist.getNth(n))
	llist.reverse()

	llist.printList()
