n=int(input())
l=[int(x) for x in input().split()]
for i in range(len(l)):
	c=l.count(l[i])
	if c==1:
		print(l[i])
		break
