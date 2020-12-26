# n WAY SET ASSOCIATIVE
print()
print(" 					  ONE LEVEL CACHE // n WAY SET ASSOCIATIVE MAPPING IMPLEMENTATION									")
print()
print()

def cachedisp():
	
	print("--------------------------------------------CACHE--MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	TAG  	    	     SET NO.         			 DATA")
	print()
	
	for i in range(CL//n):
		for j in range(n):
			print("  "+str((i)*n+j)+"				"+tag[i][j][0]+"			"+str(i)+"		  		",end=" ")
			for k in range(B):
				print(cachetemp[i][j][k],end=" ")
			print()
	
print()

N=int(input("Enter main memory size: "))
print()
CL=int(input("Enter number of cache lines: "))
print()
B=int(input("Enter block size: "))
print()
n=int(input("Enter 'n': "))

print()

cache_mem=[]
cachetemp=[]
tag=[]
tagtemp=[]

for i in range(CL//n):
	cache_mem.append([])
	tag.append([])
	cachetemp.append([])
	tagtemp.append([])

for i in range(len(cache_mem)): 		
	for j in range(n):
		cache_mem[i].append(["NULL"]*B)
		tag[i].append(["NULL"])
		cachetemp[i].append(["NULL"]*B)
		tagtemp[i].append(["NULL"])

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
		print("Block no.: "+str(block_no)+" ("+str(int(block_no,2))+")")
		
		set_no=block_no[len(block_no)-len(bin(CL//n)[2:])+1:]
		print("Set no.: "+str(set_no)+" ("+str(int(set_no,2))+")")
		
		tag_no=block_no[:len(block_no)-len(bin(CL//n)[2:])+1]
		print("Tag: "+str(tag_no)+" ("+str(int(tag_no,2))+")")
		
		set_index=int(set_no,2)
		print()

		if inptype=='w':

			chk=0
		
			for i in range(len(tag[set_index])):
			
				if tag[set_index][i]==[tag_no]:
					chk=1
					break
		
			if chk==1:
			
				print("ADDRESS FOUND IN CACHE")
				print()
				print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE")
				cache_mem[set_index][i][int(block_offset,2)]=dataa
				cachetemp[set_index][cachetemp[set_index].index(cache_mem[set_index][i])][int(block_offset,2)]=dataa
				for i in range(len(cache_mem[set_index])):
					if tag[set_index][i]==[tag_no]:
						temp1=cache_mem[set_index][i]
						temp2=tag[set_index][i]
						break
			
				for j in range(i+1,len(cache_mem[set_index])):
					cache_mem[set_index][j-1]=cache_mem[set_index][j]
					tag[set_index][j-1]=tag[set_index][j]
			
				cache_mem[set_index][-1]=temp1
				tag[set_index][-1]=temp2
		
			else:
			
				print("ADDRESS NOT FOUND IN CACHE")
				print()
				print("LOADING DATA IN CACHE MEMORY")
				print()
				print("REPLACING DATA IN CACHE MEMORY AT SET NO. ",end="")
				print(set_index)
				print()
				print("LOADING BLOCK NO. "+str(int(block_no,2))+" IN CACHE MEMORY")
				print()
				print("REPLACING DATA IN CACHE MEMORY AT LINE NO. ",end="")
	
				flag=0
			
				for i in range(len(cache_mem[set_index])):
				
					if cache_mem[set_index][i]==["NULL"]*B:
						cache_mem[set_index][i]=["NULL"]*B
						cachetemp[set_index][i]=["NULL"]*B
						tag[set_index][i]=[tag_no]
						tagtemp[set_index][i]=[tag_no]
						print(str(set_index*n+i))
						print()
						print("REPLACED ADDRESS IN CACHE MEMORY: ")
						print("Line was empty, no block found!")
						print()
						print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE")
						cache_mem[set_index][i][int(block_offset,2)]=dataa
						cachetemp[set_index][i][int(block_offset,2)]=dataa
						flag=1
						break				
			
				if flag==0:
						
					temp=tag[set_index][0]
					cachetemp[set_index][cachetemp[set_index].index(cache_mem[set_index][0])]=["NULL"]*B 
					cachetemp[set_index][cachetemp[set_index].index(cache_mem[set_index][0])][int(block_offset,2)]=dataa
					tagtemp[set_index][tagtemp[set_index].index(tag[set_index][0])]=[tag_no]   

					for j in range(1,len(cache_mem[set_index])):
						cache_mem[set_index][j-1]=cache_mem[set_index][j]
						tag[set_index][j-1]=tag[set_index][j]

					cache_mem[set_index][-1]=["NULL"]*B
					cache_mem[set_index][-1][int(block_offset,2)]=dataa
					tag[set_index][-1]=[tag_no]
					print(str(set_index*n+cachetemp[set_index].index(cache_mem[set_index][i])))
					print()
					print("REPLACED ADDRESS IN CACHE MEMORY:")
					print("BLOCK NO.: "+str(*temp)+set_no)
					print()
					print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE")

		else:

			chk=0
		
			for i in range(len(tag[set_index])):
			
				if tag[set_index][i]==[tag_no]:
					chk=1
					break
		
			if chk==1:

				print("CACHE HIT!!! ADDRESS FOUND IN CACHE")
				print()
				print("LOADING DATA FROM CACHE MEMORY")
				print()
				print("LOADING DATA FROM SET NO. "+str(set_index)+" IN CACHE MEMORY")
				print()
				print("LOADING DATA FROM LINE NO. "+str(set_index*n+cachetemp[set_index].index(cache_mem[set_index][i]))+" IN CACHE MEMORY")
				print()
				print("DATA: ",end=" ")
				print(str(cache_mem[set_index][i][int(block_offset,2)]))
				
				for i in range(len(cache_mem[set_index])):
					if tag[set_index][i]==[tag_no]:
						temp1=cache_mem[set_index][i]
						temp2=tag[set_index][i]
						break
			
				for j in range(i+1,len(cache_mem[set_index])):
					cache_mem[set_index][j-1]=cache_mem[set_index][j]
					tag[set_index][j-1]=tag[set_index][j]
			
				cache_mem[set_index][-1]=temp1
				tag[set_index][-1]=temp2

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