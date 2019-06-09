import operator
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l1={}
for i in range(0,len(l)):
	d=abs(l[i]-k)
	if d!=0:
		l1.update({l[i]:d})
sorted_x = sorted(l1.items(), key=operator.itemgetter(1))
l2=sorted_x[:3]
l3=[i[0] for i in l2]
print(*l3)
