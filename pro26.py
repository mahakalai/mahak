x=int(input())
lis=[int(x) for x in input().split()]
lis2=[]
lis1=[]
for i in range(0,len(lis)-1):
	if lis[i]<lis[i+1]:
		if lis[i] not in lis2:
			lis2.append(lis[i])
		lis2.append(lis[i+1])
		c=len(lis2)
		lis1.append(c)
	else:
		lis2=[]
print(max(lis1))		
