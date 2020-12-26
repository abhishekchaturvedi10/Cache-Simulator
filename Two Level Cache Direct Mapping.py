#TDM
print()
print("						  TWO LEVEL CACHE // DIRECT MAPPING IMPLEMENTATION											")
print()
print()

def L1disp():
	print("--------------------------------------------LEVEL--1--CACHE--MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	   TAG  	    		         	DATA")
	print()
	for i in range(CL):
		print("  "+str(i)+" 		   		   ",end="")
		print(*tag1[i],end="")
		print(" 		          		",end="")
		for j in range(B):
			print(L1[i][j],end=" ")
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

print()

N=int(input("Enter main memory size: "))
print()
CL=int(input("Enter number of cache lines: "))
print()
B=int(input("Enter block size: "))
print()

print()

L1=[]
L2=[]
tag1=[]
tag2=[]

for i in range(2*CL):
	if i<CL:
		L1.append(["NULL"]*B)				
		tag1.append(["NULL"])
		L2.append(["NULL"]*B)
		tag2.append(["NULL"])
	else:
		L2.append(["NULL"]*B)
		tag2.append(["NULL"])


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
		print("INVALID ADDRESS!")
	
	else:

		print("ADDRESS BREAKDOWN: ")
		print()
		
		word_no=int(add,2)
		print("Word No.: "+add+" ("+str(word_no)+")")
		
		block_offset=add[len(bin(N)[2:])-len(bin(B)[2:]):]
		print("Block Offset: "+block_offset+" ("+str(int(block_offset,2))+")")
		
		block_no=add[:len(bin(N)[2:])-len(bin(B)[2:])]
		print("Block No.: "+block_no+" ("+str(int(block_no,2))+")")
		
		line_no1=block_no[len(block_no)-len(bin(CL)[2:])+1:]
		print("Line 1 No.: "+line_no1+" ("+str(int(line_no1,2))+")")

		line_no2=block_no[len(block_no)-len(bin(2*CL)[2:])+1:]
		print("Line 2 No.: "+line_no2+" ("+str(int(line_no2,2))+")")
		
		tag_no1=block_no[:len(block_no)-len(bin(CL)[2:])+1]
		print("Tag 1: "+tag_no1+" ("+str(int(tag_no1,2))+")")

		tag_no2=block_no[:len(block_no)-len(bin(2*CL)[2:])+1]
		print("Tag 2: "+tag_no2+" ("+str(int(tag_no2,2))+")")
		
		line_index1=int(line_no1,2)
		line_index2=int(line_no2,2)
		
		print()

		if (tag1[line_index1]==[] or tag1[line_index1][0]!=tag_no1) and inptype=='w':

			if tag2[line_index2]==[] or tag2[line_index2][0]!=tag_no2:
			
				print("ADDRESS NOT FOUND IN CACHE")
				print()
				print("LOADING DATA IN CACHE MEMORY")
				print()
				print("REPLACING DATA IN CACHE MEMORY AT LINE NO. "+str(line_index1)+" IN L1")
				print()
				print("REPLACING DATA IN CACHE MEMORY AT LINE NO. "+str(line_index2)+" IN L2")
				print()
				print("LOADING BLOCK NO. "+str(int(block_no,2))+" IN L1 AND L2")
				print()
				print("DATA LOADED IN CACHE MEMORY")
				print()
				print("REPLACED ADDRESS IN L1: ",end="")
				
				if tag1[line_index1]==["NULL"]:
					print("Line was empty, no block found!")
				else :
					print("BLOCK NO. "+tag1[line_index1][0]+line_no1)
				
				print("REPLACED ADDRESS IN L2: ",end="")

				if tag2[line_index2]==["NULL"]:
					print("Line was empty, no block found!")
				else :
					print("BLOCK NO.: "+tag2[line_index2][0]+line_no2)
						
				tag1[line_index1]=[tag_no1]
				tag2[line_index2]=[tag_no2]
				L1[line_index1]=["NULL"]*B
				L2[line_index2]=["NULL"]*B
				L1[line_index1][int(block_offset,2)]=dataa
				L2[line_index2][int(block_offset,2)]=dataa

				print()
				print("DATA LOADED IN L1 AND L2")
				print()
				print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
				print()
				print("WORD NO. "+str(word_no)+" UPDATED IN L1 AND L2")
				
			else:

				print("ADDRESS FOUND IN CACHE MEMORY")
				print()
				print("ADDRESS FOUND IN L2")
				print()
				print("LOADING DATA FROM L2 INTO L1")
				print()
				print("LOADING DATA FROM LINE NO. "+str(line_index2)+" IN L2")
				print()
				print("REPLACING DATA IN CACHE MEMORY AT LINE NO. "+str(line_index1)+" IN L1")
				print()
				print("LOADING BLOCK NO. "+str(int(block_no,2))+" IN L1")
				print()
				print("DATA LOADED IN L1")
				print()
				print("REPLACED ADDRESS IN L1: ",end="")
				
				if tag1[line_index1]==["NULL"]:
					print("Line was empty, no block found!")
				else :
					print("BLOCK NO.: "+tag1[line_index1][0]+line_no1)
						
				tag1[line_index1]=[tag_no1]
				L1[line_index1]=["NULL"]*B
				L1[line_index1][int(block_offset,2)]=dataa
				L2[line_index2][int(block_offset,2)]=dataa

				print()
				print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
				print()
				print("WORD NO. "+str(word_no)+" UPDATED IN L1 AND L2")
					
		elif tag1[line_index1][0]==tag_no1 and inptype=='w':
			
			print("ADDRESS FOUND IN CACHE MEMORY")
			print()
			print("ADDRESS FOUND IN L1")
			print()
			print("ADDRESS FOUND AT LINE NO. "+str(line_index1)+" IN L1")
			print()
			print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
			print()
			L1[line_index1][int(block_offset,2)]=dataa
			print("WORD NO. "+str(word_no)+" UPDATED IN L1")
			print()

			if tag2[line_index2][0]==tag_no2:

				print("ADDRESS FOUND IN CACHE IN L2 ALSO")
				print()
				print("ADDRESS FOUND AT LINE NO. "+str(line_index2)+" IN L2")
				print()
				print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
				print()
				print("WORD NO. "+str(word_no)+" UPDATED IN L2 ALSO")
				L2[line_index2][int(block_offset,2)]=dataa

		else:

			if (tag1[line_index1]==[] or tag1[line_index1][0]!=tag_no1):
				
				if tag2[line_index2]==[] or tag2[line_index2][0]!=tag_no2:
					
					print("CACHE MISS!!!")
					print("ADDRESS NOT FOUND IN CACHE MEMORY!")

				else:

					print("CACHE HIT!!!")
					print()
					print("ADDRESS FOUND IN CACHE IN L2 AT LINE NO. "+str(line_index2))
					print()
					print("DATA: ",end="")
					print(L2[line_index2][int(block_offset,2)])

			else:

				print("CACHE HIT!!!")
				print()
				print("ADDRESS FOUND IN L1 AT LINE NO. "+str(line_index1))
				print()
				print("DATA: ",end="")
				print(L1[line_index1][int(block_offset,2)])

	print()
	L1disp()
	print()
	L2disp()
	print()

cont='y'
while cont=='y':
	f()
	cont=input("continue? (y/n) ")
	print()