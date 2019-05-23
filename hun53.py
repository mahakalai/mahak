s,k=map(str,input().split())
n=int(k)
l=list(s)
l1=[]
s=""
for i in range(len(l)):
	if len(l[0:n])==n:
		l1.append(l[0:n])
	l.remove(l[0])
for i in range(0,len(l1)-1):
	s1=s.join(l1[i])
	print(s1,end=" ")
s1=s.join(l1[-1])
print(s1)
