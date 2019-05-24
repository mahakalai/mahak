n=int(input())
l=[int(x) for x in input().split()]
l1=[]
for i in range(0,len(l)-1):
	if l[i]>l[i+1]:
		l1.append(l[i+1])
	else:
		l1.append("-1")
l1.append("-1")	
print(*l1)
