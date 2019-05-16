n=int(input())
l=[]
for i in range(0,n):
	s=input()
	l.append(s)
c=[]
for i in zip(*l):
    if i.count(i[0])==len(i):
        c.append(i[0])
    else:
        break
print(''.join(c))
