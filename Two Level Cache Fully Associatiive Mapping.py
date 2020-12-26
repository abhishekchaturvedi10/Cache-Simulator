#TAM
print()
print("						  TWO LEVEL CACHE // FULLY ASSOCIATIVE MAPPING IMPLEMENTATION											")
print()
print()

class BlockAddress:
	
	def __init__(self, blockno):
		self.blockno = blockno
		self.next = None
		self.prev = None

class CacheList:
	
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = BlockAddress(new_data)
		new_node.next = self.head
		
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

	def lastNode(self, blockaddress):
		while(blockaddress.next is not None):
			blockaddress = blockaddress.next
		return blockaddress
 
	def getnode(self, blockaddress,x):
		while(blockaddress.blockno != x):
			blockaddress = blockaddress.next
		return blockaddress
 
	def deleteNode(self, dele):
		if self.head is None or dele is None:
			return
		if self.head == dele:
			self.head = dele.next
		if dele.next is not None:
			dele.next.prev = dele.prev
		if dele.prev is not None:
			dele.prev.next = dele.next

print()

N=int(input("Enter main memory size: "))
print()
CL=int(input("Enter number of cache lines: "))
print()
B=int(input("Enter block size: "))
print()

block_address1=[]
address_list1=CacheList()
BA1={}
block_address2=[]
address_list2=CacheList()
BA2={}

for i in range(2*CL):
	block_address2.append("NULL")
	if i<CL:
		block_address1.append("NULL")

def L1disp():
	print("--------------------------------------------LEVEL--1--CACHE--MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	   TAG  	    		         	DATA")
	print()
	for i in range(CL):
		print("  "+str(i)+" 		   		   ",end="")
		print(block_address1[i],end="")
		print(" 		          		",end="")
		if block_address1[i] in BA1:
			for j in range(B):
				print(BA1[block_address1[i]][j][0],end=" ")
		else:
			for j in range(B):
				print("NULL",end=" ")
		print()

def L2disp():
	print("--------------------------------------------LEVEL--2--CACHE--MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	   TAG  	    		         	DATA")
	print()
	for i in range(2*CL):
		print("  "+str(i)+" 		   		   ",end="")
		print(block_address2[i],end="")
		print(" 		          		",end="")
		if block_address2[i] in BA2:
			for j in range(B):
				print(BA2[block_address2[i]][j][0],end=" ")
		else:
			for j in range(B):
				print("NULL",end=" ")
		print()

def f():
	
	inptype=input("write(w)/read(r): ")

	print()

	if inptype=='r':
		add=input("Enter address in binary form: ")

	else:
		add=input("Enter address in binary form: ")
		dataa=input("Enter data: ")
		
	print()
	
	if(len(add)!=len(bin(N)[2:])-1):
		print("Invalid address")
	
	else:
		
		print("ADDRESS BREAKDOWN: ")
		print()

		word_no=int(add,2)
		print("Word No.: "+str(add)+" ("+str(word_no)+")")
		
		block_offset=add[len(bin(N)[2:])-len(bin(B)[2:]):]
		print("Block Offset: "+str(block_offset)+" ("+str(int(block_offset,2))+")")
		
		block_no=add[:len(bin(N)[2:])-len(bin(B)[2:])]
		print("Tag: "+str(block_no)+" ("+str(int(block_no,2))+")")
		
		print()
		
		if block_no in BA1 and inptype=='r':
			
			print("CACHE HIT!!! ADDRESS FOUND")
			print()
			print("LOADING DATA FROM L1")
			print()
			print("LOADING DATA FROM LINE NO. "+str(block_address1.index(block_no))+" IN L1")
			print()
			print("LOADING DATA FROM BLOCK NO. "+block_no+" ("+str(int(block_no,2))+")"+" IN L1")
			print()
			print("DATA: ",end=" ")
			print(str(block_address1[block_no][int(block_offset,2)]))
			address_list1.deleteNode(address_list1.getnode(address_list1.head,block_no))
			address_list1.push(block_no)

		elif block_no in BA1 and inptype=='w':

			print("ADDRESS FOUND IN CACHE IN L1")
			print()
			print("ADDRESS FOUND AT LINE NO. "+str(block_address1.index(block_no))+" IN L1")
			print()
			print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
			print()
			BA1[block_no][int(block_offset,2)]=[dataa]
			print("WORD NO. "+str(word_no)+" UPDATED IN L1")
			address_list1.deleteNode(address_list1.getnode(address_list1.head,block_no))
			address_list1.push(block_no)

			if block_no in BA2:

				print("ADDRESS FOUND IN CACHE IN L2 ALSO")
				print()
				rint("ADDRESS FOUND AT LINE NO. "+str(block_address2.index(block_no))+" IN L2")
				print()
				print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
				print()
				BA2[block_no][int(block_offset,2)]=[dataa]
				print("WORD NO. "+str(word_no)+" UPDATED IN L2")
				address_list2.deleteNode(address_list2.getnode(address_list2.head,block_no))
				address_list2.push(block_no)

		elif block_no in BA2 and block_no not in BA1 and inptype=='w':

			print("ADDRESS FOUND IN L2")
			print()
			print("LOADING DATA FROM L2 INTO L1")
			print()
			print("LOADING DATA FROM LINE NO. "+str(block_address2.index(block_no))+" IN L2")
			print()
			print("REPLACING DATA IN L1 AT LINE NO. ",end="")
			
			if len(BA1)<CL:
				print(len(BA1))
				block_address1[len(BA1)]=block_no
			else:
				print(block_address1.index(address_list1.lastNode(address_list1.head).blockno))
				block_address1[block_address1.index(address_list1.lastNode(address_list1.head).blockno)]=block_no
			print()
			print("LOADING BLOCK NO. "+str(int(block_no,2))+" IN L1")
			print()
			
			print("REPLACED ADDRESS IN L1: ",end="")

			if len(BA1)<CL:
				
				BA1[block_no]=[["NULL"]]*B
				address_list1.push(block_no)
				print("Line was empty, no block found!")

			else:

				print("BLOCK NO.: "+address_list1.lastNode(address_list1.head).blockno)
				del block_address1[address_list1.lastNode(address_list1.head).blockno]
				address_list1.deleteNode(address_list1.lastNode(address_list1.head))
				BA1[block_no]=[["NULL"]]*B
				address_list1.push(block_no)

			print("DATA LOADED IN L1")
			print()
			print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
			print()
			print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE IN L1 AND L2")
			BA1[block_no][int(block_offset,2)]=[dataa]
			BA2[block_no][int(block_offset,2)]=[dataa]

			address_list2.deleteNode(address_list2.getnode(address_list2.head,block_no))
			address_list2.push(block_no)

		elif block_no in BA2 and block_no not in BA1 and inptype=='r':

			print("CACHE HIT!!!")
			print("ADDRESS FOUND IN L2")
			print()
			print("LOADING DATA FROM L2")
			print()
			print("LOADING DATA FROM LINE NO. "+str(block_address2.index(block_no))+" IN L2")
			print()
			print("LOADING DATA FROM BLOCK NO. "+block_no+" ("+str(int(block_no,2))+")"+" IN L2")
			print()
			address_list2.deleteNode(address_list2.getnode(address_list2.head,block_no))
			address_list2.push(block_no)
			print("DATA: ",end=" ")
			print(str(*BA2[block_no][int(block_offset,2)]))

		else:

			if inptype=='w':
			
				print("ADDRESS NOT FOUND IN CACHE")
				print()
				print("LOADING DATA IN L1 AND L2")
				print()
				print("REPLACING DATA IN L1 AT LINE NO. ",end="")
				if len(BA1)<CL:
					print(len(BA1))
					block_address1[len(BA1)]=block_no
				else:
					print(block_address1.index(address_list1.lastNode(address_list1.head).blockno))
					block_address1[block_address1.index(address_list1.lastNode(address_list1.head).blockno)]=block_no
				print()
				print("REPLACING DATA IN L2 AT LINE NO. ",end="")
				if len(BA2)<2*CL:
					print(len(BA2))
					block_address2[len(BA2)]=block_no
				else:
					print(block_address2.index(address_list2.lastNode(address_list2.head).blockno))
					block_address2[block_address2.index(address_list2.lastNode(address_list2.head).blockno)]=block_no
				print()
				print("LOADING BLOCK NO. "+str(int(block_no,2))+" IN L1 AND L2")
				print()
				print("DATA LOADED IN L1 AND L2")
				print()
				print("REPLACED ADDRESS IN L1: ",end="")
			
				if len(BA1)<CL:
				
					BA1[block_no]=[["NULL"]]*B
					print("Line was empty, no block found!")
					address_list1.push(block_no)
			
				else:
				
					print("BLOCK NO.: "+address_list1.lastNode(address_list1.head).blockno)
					del BA1[address_list1.lastNode(address_list1.head).blockno]
					address_list1.deleteNode(address_list1.lastNode(address_list1.head))
					BA1[block_no]=[["NULL"]]*B
					address_list1.push(block_no)

				print("REPLACED ADDRESS IN L2: ",end="")

				if len(BA2)<2*CL:
				
					BA2[block_no]=[["NULL"]]*B
					print("Line was empty, no block found!")
					address_list2.push(block_no)
			
				else:
				
					print("BLOCK NO.: "+address_list2.lastNode(address_list2.head).blockno)
					del BA2[address_list2.lastNode(address_list2.head).blockno]
					address_list2.deleteNode(address_list2.lastNode(address_list2.head))
					BA2[block_no]=[["NULL"]]*B
					address_list2.push(block_no)
				
				print()
				print("DATA LOADED IN L1 AND L2")
				print()
				print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
				print()
				print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE IN L1 AND L2")
				BA1[block_no][int(block_offset,2)]=[dataa]
				BA2[block_no][int(block_offset,2)]=[dataa]

			else:
				print("CACHE MISS!!!")
				print("ADDRESS NOT IN CACHE MEMORY")

	print()
	L1disp()
	print()
	L2disp()

cont='y'
while cont=='y':
	f()
	print()
	cont=input("continue? (y/n) ")
	print()