n=int(input())
l=[int(a) for a in input().split()]
l2=sorted(l)
for i in range(0,len(l2)-1):
		print(l2[i],end=" ")
print(l2[-1])
	
	
	
