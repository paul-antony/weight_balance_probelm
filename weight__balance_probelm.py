# Given a list of N positive weights
#divide the list into two lists such that the sum of weights in both lists are equal

#The problem is solved using dynamic approch

#find_subset finds a subset from list weights whoes sum is goal
#returns list of subset if found else empty list
def find_subset(weight,n,goal): 
     
    #binary 2D table to find subset  
	table=([[False for i in range(goal+1)]  
	for i in range(n+1)]) 
      
    # making first colum true 
	for i in range(n+1): 
		table[i][0] = True
          
	# making first row false
	for i in range(1,goal+1): 
		table[0][i]=False
              
	# Fill the subset table 
	for i in range(1,n+1): 
		for j in range(1,goal+1): 
			if j<weight[i-1]: 
				table[i][j] = table[i-1][j] 
			if j>=weight[i-1]: 
				table[i][j] = (table[i-1][j] or 
				table[i - 1][j-weight[i-1]]) 
      
	#uncomment this code to print table  
	#for i in range(n+1): 
	#	for j in range(goal+1): 
	#		print (table[i][j],end=" ") 
	#	print()

	subset = []
	if table[n][goal]:
		j = goal;
		for i in range(n,0,-1):
			if not table[i-1][j]:
				subset.append(weight[i-1])
				j -= weight[i-1];
     
	return subset 

	
#splits weights into two grops of equal sum
def balance_weight(weight):
	goal = int(sum(weight)/2)
	n =len(weight)
	subset_1 = find_subset(weight,n,goal)

	subset_2 = [x for x in weight]

	for i in subset_1:
		subset_2.remove(i)

	return subset_1, subset_2



if __name__=='__main__': 
	weight = [3,4,2,4,5] 
	subset_1, subset_2 =  balance_weight(weight)
	print(subset_1)
	print(subset_2)

