n=int(input())
l=[int(x) for x in input().split()]
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		sum=l[i]+l[j]
		if sum==0 or sum==1:
			print(l[i],l[j])
			break
