n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in l:
	 co=l.count(i)
	 if co==k:
	 	print(i)
	 	break
