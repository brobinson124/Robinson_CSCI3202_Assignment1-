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
			
class MyTree:
	def __init__(self, rootkey):

		self.root = MyNode(rootkey, None, None, None)
			
	def add(self, value, parentValue):
		#search for parentValue
		if parentValue > self.root.intkey:
			#go right
			add(self, parentValue, self.root.r.intkey)
		if parentValue < self.root.intkey:
			add(self, parentValue, self.root.l.intkey)
		if parentValue == self.root.intkey:
			
		
		
		
		
		#if (value > self.root.intkey):
			##go right
			#if(self.root.r == None):
				#newNode = MyNode(value, None, None, self.root)
				#self.root.r = newNode
			#else:
				#add(self, value, root.rc.intkey)
				
		#if (value < self.root.intkey):
			##go left
			#if(self.root.l == None):
				#newNode = MyNode(value, None, None, self.root)
				#self.root.l = newNode
	

	def delete(self, value):
		self.intkey = value #have to search to see if it's in there
		if (self.r != 0 ) or (self.l != 0):
			print("Parent has two children, node not added")
		else:
			print("Node not found")
	def printTree(self):
		print("Parent Key Value: ",self.p)
		print("Left Key Value: ", self.l, "Right Key Value: ", self.r)
		
#Tree Test

root = MyNode(5, 4, 6, None)
tree = MyTree(root, True)

	

    
