s=input()
l=s.split(" ")
l1=[]
for i in l:
	m=str(i)
	m1=m[::-1]
	l1.append(m1)
	l1.append(" ")
for i in range(0,len(l1)-1):
	print(l1[i],end="")
