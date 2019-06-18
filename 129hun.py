n=int(input())
l=list(map(int,input().split()))
c=1
for i in l:
	if l.count(i)>c:
		n1=i
		c=l.count(i)
print(n1)		
