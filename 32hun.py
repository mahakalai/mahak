n=int(input())
l=list(map(int,input().split()))
l2=l
l1=[]
for i in range(0,len(l)):
	if i%2!=0:
		l1.append(l[i])
while len(l1)>1:
	l=l1
	l1=[]
	for i in range(0,len(l)):
		if i%2!=0:
			l1.append(l[i])
print(l2.index(l1[0]))
