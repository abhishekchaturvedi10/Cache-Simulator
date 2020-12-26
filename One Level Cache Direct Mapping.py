#DIRECT MAPPING 
print()
print("						ONE LEVEL CACHE // DIRECT MAPPING IMPLEMENTATION											")
print()
print()

N=int(input("Enter main memory size: "))
print()
CL=int(input("Enter number of cache lines: "))
print()
B=int(input("Enter block size: "))
print()

cache_mem=[]
tag=[]

for i in range(CL):
	cache_mem.append([])			
	tag.append(["NULL"])
for i in range(CL):
	for j in range(B):
		cache_mem[i].append("NULL")


def cachedisp():

	print("--------------------------------------------CACHE--MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	   TAG  	    		         			DATA")
	print()
	for i in range(CL):
		print("  "+str(i)+" 		   		   ",end="")
		print(*tag[i],end="")
		print(" 		          		",end="")
		if tag[i][0]!="NULL":
			print("			",end="")
			print(*cache_mem[i])
		else:
			print(" 		",end="")
			print(*cache_mem[i])

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
		print("Word No.: "+add+" ("+str(word_no)+")")
		
		block_offset=add[len(bin(N)[2:])-len(bin(B)[2:]):]
		print("Block Offset: "+block_offset+" ("+str(int(block_offset,2))+")")
		
		block_no=add[:len(bin(N)[2:])-len(bin(B)[2:])]
		print("Block No.: "+block_no+" ("+str(int(block_no,2))+")")
		
		line_no=block_no[len(block_no)-len(bin(CL)[2:])+1:]
		print("Line No.: "+line_no+" ("+str(int(line_no,2))+")")
		
		tag_no=block_no[:len(block_no)-len(bin(CL)[2:])+1]
		print("Tag :"+tag_no+" ("+str(int(tag_no,2))+")")
		print()
		
		line_index=int(line_no,2)
		
		print()

		if inptype=='w':

			if tag[line_index]==["NULL"] or tag[line_index][0]!=tag_no:
			
				print("ADDRESS NOT FOUND IN CACHE")
				print()
				print("LOADING DATA IN CACHE MEMORY")
				print()
				print("REPLACING DATA IN CACHE MEMORY AT LINE NO. "+str(line_index))
				print()
				print("LOADING BLOCK NO. "+str(int(block_no,2))+" IN CACHE MEMORY")
				print()
				print("DATA LOADED IN CACHE MEMORY")
				print()
				tag[line_index]=[tag_no]
				cache_mem[line_index]=["NULL"]*B
				cache_mem[line_index][int(block_offset,2)]=dataa
				print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE")

			elif tag[line_index][0]==tag_no:
				
				print("ADDRESS FOUND IN CACHE")
				print()
				cache_mem[line_index][int(block_offset,2)]=dataa
				print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE")

		else:

			if tag[line_index][0]==tag_no:
				
				print("CACHE HIT!!! ADDRESS FOUND")
				print()
				print("LOADING DATA FROM LINE NO. "+str(line_index)+" IN CACHE MEMORY")
				print()
				print("LOADING DATA FROM BLOCK NO. "+str(int(block_no,2))+" IN CACHE MEMORY")
				print()
				print("DATA: ",end=" ")
				print(str(cache_mem[line_index][int(block_offset,2)]))
				print()
			
			else:
				
				print("CACHE MISS!!! ADDRESS NOT FOUND")
				print()

	print()
	cachedisp()
	print()
	
cont='y'
while cont=='y':
	f()
	cont=input("continue? (y/n) ")
	print()