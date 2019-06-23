n=int(input())
s=str(n)
l=list(s)
k=int(l[0])
m=int(l[-1])
sum=(m**k)
for i in range(0,len(l)-1):
	m=int(l[i])
	k=int(l[i+1])
	sum=sum+(m**k)
print(sum)
#ma
