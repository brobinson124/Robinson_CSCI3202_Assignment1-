#Assignment1


#Problem 1
#impliment a queue

import queue

q = queue.Queue()
test = [1,2,3,4,5,6,7,8,9,10]
for x in test:
	if isinstance(x, int):
		q.put(x)
	else:
		print ('Ints')
		quit()
while q.qsize() > 0:
	print ('D-qed: ',q.get())

#Problem 2 
#implement a stack

import sys

class mystack:
	def __init__(self,data):
		self.data = data
	def push(self,number):
		self.data.append(number)
	def pop(self):
		self.data.pop()
	def checkSize(self):
		return len(self.data)

#stack test
stacky = mystack([])
test = [1,2,3,4,5,6,7,8,9,10]
for x in test:
    stacky.push(x)
y = 0
while stacky.checkSize() > 0:
	print(stacky.data[(stacky.checkSize()-1)])
	stacky.pop()

#Problem 3
#Make a Tree

class MyNode:
  
	def __init__(self, intkey, l, r, p):
		self.intkey = intkey
		self.l = l
		self.r = r
		self.p = p
		
	def getChildren(self):
		return [self.l, self.r]
			
class MyTree:
	def __init__(self, rootkey):

		self.root = MyNode(rootkey, None, None, None)
			
	def checkTree(self, value, parentValue, root):
		if root == None:
			return False
		if root.intkey == parentValue:
			if root.l == None:
				newNode = MyNode(value, None, None, root)
				root.l = newNode
				print("Added: ", value," Under Parent: ",root.intkey)
				return newNode
			elif root.r == None:
				newNode = MyNode(value, None, None, root)
				root.r = newNode
				print("Added: ", value," Under Parent: ",root.intkey)
				return newNode
			else:
				print("Parent has two children, node not added.")
				return False
		else:
			for child in root.getChildren():
				add_temp = self.checkTree(value, parentValue, child)
				if add_temp:
					return add_temp
		
		
	def add(self, value, parentValue):
		if self.root == None:
			print("Added new root")
			newNode = MyNode(value, None, None, None)
			self.root = newNode
		if self.root.intkey == parentValue:
			if self.root.l == None:
				newNode = MyNode(value, None, None, self.root)
				self.root.l = newNode
				print("Added: ", value," Under Parent: ",self.root.intkey)
				return True
			elif self.root.r == None:
				newNode = MyNode(value, None, None, self.root)
				self.root.r = newNode
				print("Added: ", value," Under Parent: ",self.root.intkey)
				return True
			else:
				print("Parent has two children, node not added.")
				return False
		else:
			#recursively search through children
			for child in self.root.getChildren():
				add_node = self.checkTree(value, parentValue, child)
				if add_node:
					return add_node
		print("Node not found")
		return False
	
	def findNodeDelete(self, value, root):
		if root == None:
			return False
		if value == root.intkey:
			if root.l == None and root.r == None:
				print("Deleting Node", root.intkey)
				#update parent
				if root.p.l.intkey == value:
					root.p.l = None
				elif root.p.r.intkey == value:
					root.p.r = None
				root = None
				return True
			else:
				print("Node not deleted, has children")
				return False
		else:
			for child in root.getChildren():
				delete_node = self.findNodeDelete(value, child)
				if delete_node:
					return delete_node
			
		
		
	def delete(self, value):
		if value == self.root.intkey:
			if self.root.l == None and self.root.r == None:
				print("Deleting Root")
				self.root = None
				return True
			else:
				print("Node not deleted, has children")
				return False
		else:
			for child in self.root.getChildren():
				delete_node = self.findNodeDelete(value, child)
				if delete_node:
					return delete_node
					
		print("Node not found")
		return False
		
	def printTree(self):
		if self.root != None:
			print (self.root.intkey)
			for child in self.root.getChildren():
				self.printBranch(child)
		else: 
			return
			
	
	def printBranch(self, root):
		if root == None:
			return
		else:
			print (root.intkey)
			for child in root.getChildren():
				self.printBranch(child)
					
	
				
		
#Tree Test


tree = MyTree(5)
tree.add(6,5)
tree.add(4,5)
tree.add(7,4)
tree.add(3,7)
tree.add(8,4)
tree.add(2,8)
tree.add(9,7)
tree.add(1,3)
tree.add(10,3)

tree.printTree()

tree.delete(10)
tree.delete(1)

tree.add(18,3)

tree.printTree()

	

    
