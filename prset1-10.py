n=int(input())
l=[int(x) for x in input().split()]
s=0
for i in range(0,len(l)):
	for j in range(0,l[i]):
		s=s+j
print(s)
