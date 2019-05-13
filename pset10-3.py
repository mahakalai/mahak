n=int(input())
l=[int(x) for x in input().split()]
N=1
l1=[]
while N<len(l):
	l1.append(l[N])
	l1.append(l[N-1])
	N=N+2
if len(l)%2!=0:
	l1.append(l[-1])
for i in range(0,len(l1)-1):
	print(l1[i],end=" ")
print(l1[-1])	
