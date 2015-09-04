#Assignment1
#Brooke Robinson


#Problem 1
#impliment a queue

import Queue 
#python2 is 'Queue'
#python3 is 'queue'

q = Queue.Queue()
test = [1,2,3,4,5,6,7,8,9,10]
for x in test:
	if isinstance(x, int):
		q.put(x)
	else:
		print ('Ints')
		quit()

''''''''''''''''''''''''''''''''''''''''''
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

''''''''''''''''''''''''''''''''''''''''''

#Problem 3
#Make a Tree

class MyNode:
	#create a Node class that contains value, leftchild, rightchild,
	#and parent attributes.
  
	def __init__(self, intkey, l, r, p):
		self.intkey = intkey
		self.l = l
		self.r = r
		self.p = p
		
	def getChildren(self):
		#returns both left and right children
		return [self.l, self.r]
			
class MyTree:
	def __init__(self, rootkey):
		self.root = MyNode(rootkey, None, None, None)
		#create a new tree while setting root
			
	def checkTree(self, value, parentValue, root):
		#Recursive function that searches through tree to find
		#if parentValue exists
		
		if root == None:
			#if there is no root in tree
			return False
		if root.intkey == parentValue:
			if root.l == None:
				newNode = MyNode(value, None, None, root)
				root.l = newNode
				#print("Added: ", value," Under Parent: ",root.intkey)
				return newNode
			elif root.r == None:
				newNode = MyNode(value, None, None, root)
				root.r = newNode
				#print("Added: ", value," Under Parent: ",root.intkey)
				return newNode
			else:
				print "Parent has two children, node not added."
				return False
		else:
			for child in root.getChildren():
				add_temp = self.checkTree(value, parentValue, child)
				if add_temp:
					return add_temp
		
		
	def add(self, value, parentValue):
		if self.root == None:
			#print("Added new root")
			newNode = MyNode(value, None, None, None)
			self.root = newNode
		if self.root.intkey == parentValue:
			if self.root.l == None:
				newNode = MyNode(value, None, None, self.root)
				self.root.l = newNode
				#print("Added: ", value," Under Parent: ",self.root.intkey)
				return True
			elif self.root.r == None:
				newNode = MyNode(value, None, None, self.root)
				self.root.r = newNode
				#print("Added: ", value," Under Parent: ",self.root.intkey)
				return True
			else:
				print "Parent has two children, node not added."
				return False
		else:
			#recursively search through children
			for child in self.root.getChildren():
				add_node = self.checkTree(value, parentValue, child)
				if add_node:
					return add_node
		print "Node not found"
		return False
	
	def findNodeDelete(self, value, root):
		if root == None:
			return False
		if value == root.intkey:
			if root.l == None and root.r == None:
				#print("Deleting Node", root.intkey)
				#update parent
				if root.p.l.intkey == value:
					root.p.l = None
				elif root.p.r.intkey == value:
					root.p.r = None
				root = None
				return True
			else:
				print "Node not deleted, has children"
				return False
		else:
			for child in root.getChildren():
				delete_node = self.findNodeDelete(value, child)
				if delete_node:
					return delete_node
			
		
		
	def delete(self, value):
		if self.root == None:
			self.root = MyNode(value, None, None, None)
		if value == self.root.intkey:
			if self.root.l == None and self.root.r == None:
				#print("Deleting Root")
				self.root = None
				return True
			else:
				print "Node not deleted, has children"
				return False
		else:
			for child in self.root.getChildren():
				delete_node = self.findNodeDelete(value, child)
				if delete_node:
					return delete_node
					
		print "Node not found" 
		return False
		
	def printTree(self):
		if self.root != None:
			print self.root.intkey
			for child in self.root.getChildren():
				self.printBranch(child)
		else: 
			return
			
	
	def printBranch(self, root):
		if root == None:
			return
		else:
			print root.intkey
			for child in root.getChildren():
				self.printBranch(child)
					
''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
#Number 4
#Bring on the Graph!
#Unweighted
		
class graph:
	def __init__(self):
		self.verticies = {}
			
	def addVertex(self, value):
		#check if value already exists
		if value in self.verticies:
			print "Vertex already exists"
		else:
			self.verticies[value] = []
			
	def addEdge(self, value1, value2):
		if value1 in self.verticies and value2 in self.verticies:
			self.verticies[value1].append(value2)
			self.verticies[value2].append(value1)
		else:
			print "One or more vertices not found."
			
	def findVertex(self, value):
		if value in self.verticies:
			adj = self.verticies[value]
			print adj
		else:
			print "Not found."
			
'''''''''''''''''''''''''''''''''''''''''''''''''''
Tests
'''''''''''''''''''''''''''''''''''''''''''''''''''

#Queue Test

print "Queue Test: "
print "Enqueue and Dequeue 10 ints"
print ""
while q.qsize() > 0:
	print 'D-qed: ',q.get()


#stack test

print "-------------------------------------------"
print "Stack Test: "
print "Pop 10 ints"
print ""
stacky = mystack([])
test = [1,2,3,4,5,6,7,8,9,10]
for x in test:
    stacky.push(x)
y = 0
while stacky.checkSize() > 0:
	print stacky.data[(stacky.checkSize()-1)]
	stacky.pop()
	
	
#Tree Test

print "-------------------------------------------"
print "Tree Test"
print "add 10 ints to tree, print In-Order, delete 2 ints, print In-Order"
print ""

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

print ""

tree.printTree()

print ""

tree.delete(10)
tree.delete(1)

tree.add(18,3)

tree.printTree()

#Graph Test

print "-------------------------------------------"
print "Graph Test"
print "Add 10 vertecies, make 20 edges, print edges of five vertecies"
print ""

g = graph()
g.addVertex(1)
g.addVertex(11)
g.addVertex(12)
g.addVertex(13)
g.addVertex(14)
g.addVertex(15)
g.addVertex(16)
g.addVertex(17)
g.addVertex(18)
g.addVertex(19)
g.addVertex(100)

g.addEdge(1,12)
g.addEdge(1,13)
g.addEdge(11,14)
g.addEdge(15,11)
g.addEdge(16,100)
g.addEdge(15,17)
g.addEdge(15,12)
g.addEdge(12,13)
g.addEdge(12,14)
g.addEdge(12,16)
g.addEdge(12,17)
g.addEdge(1,100)
g.addEdge(12,100)
g.addEdge(15,100)
g.addEdge(19,12)
g.addEdge(13,100)
g.addEdge(14,100)
g.addEdge(100,19)
g.addEdge(19,18)
g.addEdge(19,17)

g.findVertex(1)
g.findVertex(12)
g.findVertex(13)
g.findVertex(14)
g.findVertex(100)

	
