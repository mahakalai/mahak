n=int(input())
l=[int(x) for x in input().split()]
l1=[]
l2=[]
for i in range(0,len(l)-1):
	j=i+1
	if l[i]<l[j]:
		l1.append(l[i])
		l1.append(l[j])
		m=list(set(l1))
	else:
		c=len(m)
		l2.append(c)
		l1=[]
print(l2)			
			
