#ASSOCIATIVE MAPPING
print()
print("						  ONE LEVEL CACHE // FULLY ASSOCIATIVE MAPPING IMPLEMENTATION											")
print()
print()

def L2disp():
	print("--------------------------------------------LEVEL--2--CACHE--MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	   TAG  	    		         DATA")
	print()
	for i in range(2*CL):
		print("  "+str(i)+" 		   		   ",end="")
		print(*tag2[i],end="")
		print(" 		          		",end="")
		for j in range(B):
			print(L2[i][j],end=" ")
		print()

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

def cachedisp1():
	
	print("--------------------------------------------CACHE MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	   TAG  	    		         		DATA")
	print()
	for i in range(CL):
		print("  "+str(i)+" 		   		   ",end="")
		print(*tag[i],end="")
		print(" 		          		",end="")
		if tag[i][0]!="_":
			print(*cache_mem[i],end=" ")
			print("   block no.: "+str(cache_mem[i][0]//B))
		else:
			print(" 		",end="")
			print(*cache_mem[i])

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


def cachedisp():
	
	print("--------------------------------------------CACHE--MEMORY------------------------------------------------")
	print()
	print()
	print("  LINE NO.		   		TAG					DATA")
	print()
	for i in range(len(block_address)):
		print("  "+str(i)+"			  	 	",end="")
		print(block_address[i],end="     		      	        ")
		print(*block_address1[block_address[i]])
	for j in range(len(block_address),CL):
		print("  "+str(j)+"     		 		",end="")
		print("NULL",end="    				")
		for i in range(B):
			print("NULL",end=" ")
		print()

print()

N=int(input("Enter main memory size: "))
print()
CL=int(input("Enter number of cache lines: "))
print()
B=int(input("Enter block size: "))
print()

block_address=[]
block_address1={}
address_list=CacheList()


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
		print("INVALID ADDRESS")
	
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

		if inptype=='w':
		
			if block_no in block_address1:
				
				print("ADDRESS FOUND IN CACHE")
				print()
				print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE")
				block_address1[block_no][int(block_offset,2)]=dataa
				address_list.deleteNode(address_list.getnode(address_list.head,block_no))
				address_list.push(block_no)

			else:
			
				print("ADDRESS NOT IN CACHE")
				print()
				print("LOADING DATA IN CACHE MEMORY")
				print()
				print("REPLACING DATA IN CACHE MEMORY AT LINE NO. ",end="")
				if len(block_address1)<CL:
					print(len(block_address1))
					block_address.append(block_no)
				else:
					print(block_address.index(address_list.lastNode(address_list.head).blockno))
					block_address[block_address.index(address_list.lastNode(address_list.head).blockno)]=block_no
				print()
				print("LOADING BLOCK NO. "+str(int(block_no,2))+" IN CACHE MEMORY")
				print()
				print("DATA LOADED IN CACHE MEMORY")
				print()
				print("REPLACED ADDRESS IN CACHE MEMORY: ")
			
				if len(block_address1)<CL:
				
					block_address1[block_no]=["NULL"]*B
					print("Line was empty, no block found!")
					address_list.push(block_no)
			
				else:
				
					print("BLOCK NO.: "+address_list.lastNode(address_list.head).blockno)
					del block_address1[address_list.lastNode(address_list.head).blockno]
					address_list.deleteNode(address_list.lastNode(address_list.head))
					block_address1[block_no]=["NULL"]*B
					address_list.push(block_no)
				print()
				print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE")
				block_address1[block_no][int(block_offset,2)]=dataa
			
		else:

			if block_no in block_address1:
				
				print("CACHE HIT!!! ADDRESS FOUND IN CACHE")
				print()
				print("LOADING DATA FROM LINE NO. "+str(block_address.index(block_no))+" IN CACHE MEMORY")
				print()
				print("LOADING DATA FROM BLOCK NO. "+str(int(block_no,2))+" IN CACHE MEMORY")
				print()
				print("DATA: ",end=" ")
				print(block_address1[block_no][int(block_offset,2)])
				address_list.deleteNode(address_list.getnode(address_list.head,block_no))
				address_list.push(block_no)

			else:

				print("CACHE MISS!!! ADDRESS NOT FOUND IN CACHE")
	
	print()
	cachedisp()
	print()

cont='y'
while cont=='y':
	f()
	cont=input("continue? (y/n) ")
	print()