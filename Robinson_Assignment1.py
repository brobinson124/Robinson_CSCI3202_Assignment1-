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

class MyTreeNode:
  
	def __init__(self, intkey, l, r, p):
		self.intkey = intkey
		self.l = l
		self.r = r
		self.p = p
	def add(self, value, parentValue):
		self.intkey = value
		if (self.p != parentValue): #pvalue is found in tree
			self.p = parentValue
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

root = MyTreeNode(0, 0, 0, 0)
	

    
