n=int(input())
l=[int(x) for x in input().split()]
for i in l:
	c=l.count(i)
	if c==1:
		print(i)
		break
