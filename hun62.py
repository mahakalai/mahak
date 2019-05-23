n=int(input())
l1=[int(x) for x in input().split()]
l2=[]
for i in range(len(l1)):
	for j in range(i+1,len(l1)):
		d=abs(l1[i]-l1[j])
		l2.append(d)
print(max(l2))		
