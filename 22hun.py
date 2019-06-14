n=int(input())
l1=list(map(int,input().split()))
k=1
l3=[]
for x in l1:
	k=k*x
for x in l1:
	l=k//x 
	l3.append(l)
print(*l3)
