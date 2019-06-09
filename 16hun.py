n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l1={}
for i in range(0,len(l)):
	d=abs(l[i]-k)
	if d!=0:
		l1.update({l[i]:d})
l2=sorted(l1)
l3=l2[:3]
print(*l3)
