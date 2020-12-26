#TSAM
print()
print(" 					  TWO LEVEL CACHE // n WAY SET ASSOCIATIVE MAPPING IMPLEMENTATION									")
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

L1=[]
L1temp=[]
L2=[]
L2temp=[]
tag1=[]
tag1temp=[]
tag2=[]
tag2temp=[]

for i in range((2*CL)//n):
	if i<CL//n:
		L1.append([])
		L1temp.append([])
		tag1.append([])
		tag1temp.append([])
		L2.append([])
		L2temp.append([])
		tag2.append([])
		tag2temp.append([])
	else:
		L2.append([])
		L2temp.append([])
		tag2.append([])
		tag2temp.append([])

for i in range(len(L2)): 		# Initialising each line in each set with empty adress in L2
	for j in range(n):
		L2[i].append([["NULL"]]*B)
		L2temp[i].append([["NULL"]]*B)
		tag2[i].append(["NULL"])
		tag2temp[i].append(["NULL"])

for i in range(len(L1)): 		# Initialising each line in each set with empty adress in L1
	for j in range(n):
		L1[i].append([["NULL"]]*B)
		L1temp[i].append([["NULL"]]*B)
		tag1[i].append(["NULL"])
		tag1temp[i].append(["NULL"])

def L1disp():
	
	print("--------------------------------------------LEVEL--1--CACHE--MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	TAG  	    	     SET NO.         			 DATA")
	print()
	
	for i in range(CL//n):
		for j in range(n):
			print("  "+str((i)*n+j)+"				"+tag1temp[i][j][0]+"			"+str(i)+"		  		",end=" ")
			for k in range(B):
				print(L1temp[i][j][k][0],end=" ")
			print()

def L2disp():
	
	print("--------------------------------------------LEVEL--2--CACHE--MEMORY--------------------------------------------------")
	print()
	print()
	print("  LINE NO.	   	 	TAG  	    	     SET NO.         			 DATA")
	print()
	
	for i in range(2*CL//n):
		for j in range(n):
			print("  "+str((i)*n+j)+"				"+tag2temp[i][j][0]+"			"+str(i)+"		  		",end=" ")
			for k in range(B):
				print(L2temp[i][j][k][0],end=" ")
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
		print("INVALID ADDRESS!")
	
	else:

		print("ADDRESS BREAKDOWN: ")
		print()
		
		word_no=int(add,2)
		print("Word No.: "+str(add)+" ("+str(word_no)+")")
		
		block_offset=add[len(bin(N)[2:])-len(bin(B)[2:]):]
		print("Block Offset: "+str(block_offset)+" ("+str(int(block_offset,2))+")")
		
		block_no=add[:len(bin(N)[2:])-len(bin(B)[2:])]
		print("Block no.: "+str(block_no)+" ("+str(int(block_no,2))+")")
		
		set_no1=block_no[len(block_no)-len(bin(CL//n)[2:])+1:]
		print("Set 1 no.: "+str(set_no1)+" ("+str(int(set_no1,2))+")")

		set_no2=block_no[len(block_no)-len(bin((2*CL)//n)[2:])+1:]
		print("Set 2 no.: "+str(set_no2)+" ("+str(int(set_no2,2))+")")
		
		tag_no1=block_no[:len(block_no)-len(bin(CL//n)[2:])+1]
		print("Tag1: "+str(tag_no1)+" ("+str(int(tag_no1,2))+")")

		tag_no2=block_no[:len(block_no)-len(bin((2*CL)//n)[2:])+1]
		print("Tag2: "+str(tag_no2)+" ("+str(int(tag_no2,2))+")")
		
		set_index1=int(set_no1,2)
		set_index2=int(set_no2,2)
		
		print()

		if inptype=='w':

				chk=0
		
				for i in range(len(tag1[set_index1])):
			
					if tag1[set_index1][i]==[tag_no1]:
						chk=1
						break
		
				if chk==1:
			
					print("ADDRESS FOUND IN CACHE")
					print()
					print("ADDRESS FOUND IN L1")
					print()
					print("ADDRESS FOUND IN SET NO. "+str(set_index1)+" IN L1")
					print()
					print("ADDRESS FOUND IN LINE NO. "+str(set_index1*n+L1temp[set_index1].index(L1[set_index1][i]))+" IN L1")
					print()
					print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
					print()
					print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN DATA IN L1")
					L1[set_index1][i][int(block_offset,2)]=[dataa]
					L1temp[set_index1][L1temp[set_index1].index(L1[set_index1][i])][int(block_offset,2)]=[dataa]
			
					for i in range(len(L1[set_index1])):
						if tag1[set_index1][i]==[tag_no1]:
							temp1=L1[set_index1][i]
							temp2=tag1[set_index1][i]
							break
			
					for j in range(i+1,len(L1[set_index1])):
						L1[set_index1][j-1]=L1[set_index1][j]
						tag1[set_index1][j-1]=tag1[set_index1][j]
			
					L1[set_index1][-1]=temp1
					tag1[set_index1][-1]=temp2

					flag=0

					for i in range(len(tag2[set_index2])):
			
						if tag2[set_index2][i]==[tag_no2]:
							flag=1
							break

					if flag==1:
			
						print("ADDRESS FOUND IN L2 ALSO")
						print()
						print("ADDRESS FOUND IN SET NO. "+str(set_index2)+" IN L2")
						print()
						print("ADDRESS FOUND IN LINE NO. "+str(set_index2*n+L2temp[set_index2].index(L2[set_index2][i]))+" IN L2")
						print()
				
						for i in range(len(L2[set_index2])):
							if tag2[set_index2][i]==[tag_no2]:
								temp1=L2[set_index2][i]
								temp2=tag2[set_index2][i]
								break
			
						for j in range(i+1,len(L2[set_index2])):
							L2[set_index2][j-1]=L2[set_index2][j]
							tag2[set_index2][j-1]=tag2[set_index2][j]
						print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
						print()
						print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN DATA IN L2 ALSO")
						L2[set_index2][-1]=temp1
						tag2[set_index2][-1]=temp2
						L2[set_index2][-1][int(block_offset,2)]=[dataa]
						L2temp[set_index2][L2temp[set_index2].index(L2[set_index2][i])][int(block_offset,2)]=[dataa]
		
				else:
			
					flag=0

					for i in range(len(tag2[set_index2])):
			
						if tag2[set_index2][i]==[tag_no2]:
							flag=1
							break

					if flag==1:
			
						print("ADDRESS FOUND IN CACHE")
						print()
						print("ADDRESS FOUND IN L2")
						print()
						print("LOADING DATA FROM L2 INTO L1")
						print()
						print("LOADING DATA FROM SET NO. "+str(set_index2)+" IN L2")
						print()
						print("LOADING DATA FROM LINE NO. "+str(set_index2*n+L2temp[set_index2].index(L2[set_index2][i]))+" IN L2")
						print()
						print("REPLACING DATA IN L1 AT SET NO. ",end="")
						print(set_index1)
						print("REPLACING DATA IN L1 AT LINE NO. ",end="")
				
						for i in range(len(L2[set_index2])):
							if tag2[set_index2][i]==[tag_no2]:
								temp1=L2[set_index2][i]
								temp2=tag2[set_index2][i]
								break
			
						for j in range(i+1,len(L2[set_index2])):
							L2[set_index2][j-1]=L2[set_index2][j]
							tag2[set_index2][j-1]=tag2[set_index2][j]
			
						L2[set_index2][-1]=temp1
						tag2[set_index2][-1]=temp2
						L2[set_index2][-1][int(block_offset,2)]=[dataa]
						L2temp[set_index2][L2temp[set_index2].index(L2[set_index2][i])][int(block_offset,2)]=[dataa]

						flag=0

						for i in range(len(L1[set_index1])):
				
							if L1[set_index1][i]==[["NULL"]]*B:
								L1[set_index][i]=[["NULL"]]*B
								L1temp[set_index][i]=[["NULL"]]*B
								L1[set_index1][i][int(block_offset,2)]=[dataa]
								L1temp[set_index1][i][int(block_offset,2)]=[dataa]
								tag1[set_index][i]=[tag_no1]
								tag1temp[set_index][i]=[tag_no1]
								print(str(set_index1*n+i))
								print()
								print("REPLACED ADDRESS IN L1: ")
								print("Line was empty, no block found!")
								print()
								print("DATA LOADED IN L1")
								print()
								print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
								print()
								print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE IN L1 AND L2")
								flag=1
								break				
			
						if flag==0:
						
							temp=tag1[set_index1][0]
							L1temp[set_index1][L1temp[set_index1].index(L1[set_index1][0])]=[["NULL"]]*B  
							tag1temp[set_index1][tag1temp[set_index1].index(tag1[set_index1][0])]=[tag_no1]   

							for j in range(1,len(L1[set_index1])):
								L1[set_index1][j-1]=L1[set_index1][j]
								tag1[set_index1][j-1]=tag1[set_index1][j]

							L1[set_index1][-1]=[["NULL"]]*B
							L1[set_index1][-1][int(block_offset,2)]=[dataa]
							tag1[set_index1][-1]=[tag_no1]
							print(str(set_index1*n+L1temp[set_index1].index(L1[set_index1][i])))
							print()
							print("REPLACED ADDRESS IN L1:")
							print("BLOCK NO.: "+str(*temp)+set_no1)
							print()
							print("DATA LOADED IN L1")
							print()
							print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
							print()
							print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE IN L1 AND L2")
							L1temp[set_index1][L1temp[set_index1].index(L1[set_index1][i])][int(block_offset,2)]=[dataa]

					else:

						print("ADDRESS NOT FOUND IN CACHE")
						print()
						print("LOADING DATA INTO L1 AND L2")
						print()
						print("REPLACING DATA IN L1 AT SET NO. ",end="")
						print(set_index1)
						print()
						print("REPLACING DATA IN L1 AT LINE NO. ",end="")

						flag=0

						for i in range(len(L1[set_index1])):
				
							if L1[set_index1][i]==[["NULL"]]*B:
								L1[set_index1][i]=[["NULL"]]*B
								L1temp[set_index1][i]=[["NULL"]]*B
								L1[set_index1][i][int(block_offset,2)]=[dataa]
								L1temp[set_index1][i][int(block_offset,2)]=[dataa]
								tag1[set_index1][i]=[tag_no1]
								tag1temp[set_index1][i]=[tag_no1]
								print(str(set_index1*n+i))
								print()
								print("REPLACED ADDRESS IN L1: ")
								print("Line was empty, no block found!")
								print()
								print("DATA LOADED IN L1")
								print()
								flag=1
								break				
			
						if flag==0:
						
							temp=tag1[set_index1][0]
							L1temp[set_index1][L1temp[set_index1].index(L1[set_index1][0])]=[["NULL"]]*B
							L1temp[set_index1][L1temp[set_index1].index(L1[set_index1][0])][int(block_offset,2)]=[dataa]  
							tag1temp[set_index1][tag1temp[set_index1].index(tag1[set_index1][0])]=[tag_no1]   

							for j in range(1,len(L1[set_index1])):
								L1[set_index1][j-1]=L1[set_index1][j]
								tag1[set_index1][j-1]=tag1[set_index1][j]

							L1[set_index1][-1]=[["NULL"]]*B
							L1[set_index1][-1][int(block_offset,2)]=[dataa]
							tag1[set_index1][-1]=[tag_no1]
							print(str(set_index1*n+L1temp[set_index1].index(L1[set_index1][i])))
							print()
							print("REPLACED ADDRESS IN L1:")
							print("BLOCK NO.: "+str(*temp)+set_no1)
							print()
							print("DATA LOADED IN L1")
							print()
						print("REPLACING DATA IN L2 AT SET NO. ",end="")
						print(set_index2)
						print()
						print("REPLACING DATA IN L2 AT LINE NO. ",end="")
				
						flag=0

						for i in range(len(L2[set_index2])):
				
							if L2[set_index2][i]==[["NULL"]]*B:
								L2[set_index2][i]=[["NULL"]]*B
								L2temp[set_index2][i]=[["NULL"]]*B
								L2[set_index2][i][int(block_offset,2)]=[dataa]
								L2temp[set_index2][i][int(block_offset,2)]=[dataa]
								tag2[set_index2][i]=[tag_no2]
								tag2temp[set_index2][i]=[tag_no2]
								print(str(set_index2*n+i))
								print()
								print("REPLACED ADDRESS IN L2: ")
								print("Line was empty, no block found!")
								print()
								print("DATA LOADED IN L2")
								print()
								print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
								print()
								print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE IN L1 AND L2")
								flag=1
								break				
			
						if flag==0:
						
							temp=tag2[set_index2][0]
							L2temp[set_index2][L2temp[set_index2].index(L2[set_index2][0])]=[["NULL"]]*B
							L2temp[set_index2][L2temp[set_index2].index(L2[set_index2][0])][int(block_offset,2)]=[dataa]
							tag2temp[set_index2][tag2temp[set_index2].index(tag2[set_index2][0])]=[tag_no2]   

							for j in range(1,len(L2[set_index2])):
								L2[set_index2][j-1]=L2[set_index2][j]
								tag2[set_index2][j-1]=tag2[set_index2][j]

							L2[set_index2][-1]=[["NULL"]]*B
							L2[set_index2][-1][int(block_offset,2)]=dataa
							tag2[set_index2][-1]=[tag_no2]
							print(str(set_index2*n+L2temp[set_index2].index(L2[set_index2][i])))
							print()
							print("REPLACED ADDRESS IN L2:")
							print("BLOCK NO.: "+str(*temp)+set_no2)
							print()
							print("DATA LOADED IN L2")
							print()
							print("UPDATING THE GIVEN ADDRESS WITH GIVEN VALUE IN CACHE MEMORY")
							print()
							print("WORD NO. "+str(word_no)+" UPDATED WITH GIVEN VALUE IN L1 AND L2")

		else:

			chk=0
		
			for i in range(len(tag1[set_index1])):
			
				if tag1[set_index1][i]==[tag_no1]:
					chk=1
					break
		
			if chk==1:
			
				print("CACHE HIT!!! ADDRESS FOUND IN CACHE")
				print()
				print("ADDRESS FOUND IN L1")
				print()
				print("ADDRESS FOUND IN SET NO. "+str(set_index1)+" IN L1")
				print()
				print("ADDRESS FOUND IN LINE NO. "+str(set_index1*n+L1temp[set_index1].index(L1[set_index1][i]))+" IN L1")
				print()
				print("DATA: ",end=" ")
				print(str(*L1[set_index1][-1][int(block_offset,2)]))
				for i in range(len(L1[set_index1])):
					if tag1[set_index1][i]==[tag_no1]:
						temp1=L1[set_index1][i]
						temp2=tag1[set_index1][i]
						break
			
				for j in range(i+1,len(L1[set_index1])):
					L1[set_index1][j-1]=L1[set_index1][j]
					tag1[set_index1][j-1]=tag1[set_index1][j]
			
				L1[set_index1][-1]=temp1
				tag1[set_index1][-1]=temp2

			else:

				flag=0

				for i in range(len(tag2[set_index2])):
			
					if tag2[set_index2][i]==[tag_no2]:
						flag=1
						break

				if flag==1:
			
					print("CACHE HIT!!! ADDRESS FOUND IN CACHE")
					print()
					print("ADDRESS FOUND IN L2")
					print()
					print("LOADING DATA FROM L2 INTO L1")
					print()
					print("LOADING DATA FROM SET NO. "+str(set_index2)+" IN L2")
					print()
					print("LOADING DATA FROM LINE NO. "+str(set_index2*n+L2temp[set_index2].index(L2[set_index2][i]))+" IN L2")
					print()
				
					for i in range(len(L2[set_index2])):
						if tag2[set_index2][i]==[tag_no2]:
							temp1=L2[set_index2][i]
							temp2=tag2[set_index2][i]
							break
			
					for j in range(i+1,len(L2[set_index2])):
						L2[set_index2][j-1]=L2[set_index2][j]
						tag2[set_index2][j-1]=tag2[set_index2][j]
			
					L2[set_index2][-1]=temp1
					tag2[set_index2][-1]=temp2
					print("DATA: ",end=" ")
					print(str(*L2[set_index2][-1][int(block_offset,2)]))


				else:

					print("CACHE MISS!!!")
					print("ADDRESS NOT FOUND IN CACHE")

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