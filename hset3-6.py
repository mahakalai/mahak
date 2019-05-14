n=int(input())
l=[int(x) for x in input().split()]
l1=l[::-1]
for i in range(0,len(l1)-1):
	print(l1[i],end="->")
print(l1[-1])
