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

class MyTrieNode:
	# Initialize some fields 
  
	def __init__(self, isRootNode):
		#The initialization below is just a suggestion.
		#Change it as you will.
		# But do not change the signature of the constructor.
		self.isRoot = isRootNode
		self.isWordEnd = False # is this node a word ending node
		#self.isRoot = False # is this a root node
		self.count = 0 # frequency count
		self.next = {}

    
