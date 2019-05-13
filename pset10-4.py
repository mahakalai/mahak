n=int(input())
s=str(n)
l1=list(s)
l=[]
for i in range(0,len(l1)):
	m=l1.count(l1[i])
	l.append(m)
if max(l)==1:
	print("no")
else:
	print("yes")
