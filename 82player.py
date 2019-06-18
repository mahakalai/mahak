n=int(input())
l=list(map(int,input().split()))
c=1
for i in l:
	c=c&i
print(c)	
