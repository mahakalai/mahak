n=int(input())
l=[int(x) for x in input().split()]
l1=[]
for i in range(0,len(l)):
	if i%2==0 and l[i]%2!=0:
		l1.append(l[i])
	elif i%2!=0 and l[i]%2==0:
		l1.append(l[i])
	else:
		continue
for i in range(0,len(l1)-1):
	print(l1[i],end=" ")
print(l1[-1])
