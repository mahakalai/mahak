n=int(input())
l=[int(x) for x in input().split()]
l1=sorted(l)
l2=l1[::-1]
for i in l2:
	print(i)
