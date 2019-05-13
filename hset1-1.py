n=int(input())
l=[int(x) for x in input().split()]
l1=[]
for i in range(0,len(l)):
	if l.count(l[i])>1 :
		l1.append(l[i])
l1= list(dict.fromkeys(l1))		
print(*l1)
