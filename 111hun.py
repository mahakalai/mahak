n=int(input())
i=0
sum=0
for j in range(n):
	l=list(map(int,input().split()))
	sum=sum+l[i]
	i=i+1
print(sum)	
